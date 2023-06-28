import numpy as np

def saglrstepvar(y,L,h,Delta,mode='multiple',gr=0):
# [t0,ta,g0,ga]=saglrstepvar(y,L,h,Delta,mode,gr)
# segmentation of independent zero mean Gaussian noise process
# with piece-wise constant variance
# 具有分段常差的独立零均值高斯噪声过程的分割

# y          input signal (column vector)
# L          size of sliding test window
# h          detection threshold
# Delta      minimum number of samples used for ML parameter estimation after change
# mode (opt) 'single' -> detect single event, 'multiple' -> detect multiple events (default)  
# gr   (opt) 1 -> display detection process, 0 -> no display (default)

# t0         scalar or vector with detected change time(s)
# ta         scalar or vector with corresponding alarm time(s)
# g0         likelihood function for determination of change times
# ga         test function of stopping rule

# -------------------------------------------------------------------------------------------

# Example:

# v=repmat([.01*ones(200,1);ones(100,1)],[10 1]); % generate true variance profile
# y=sqrt(v).*randn(size(v));                      % generate noise signal
# t0=saglrstepvar(y,50,10,10,'multiple',1);       % determine change times and plot intermediate results

# -------------------------------------------------------------------------------------------

# method: sequential application of approximated generalized likelihood-ratio (AGLR) test 
#         assumed change profile: abrupt step-like change in variance
#         the unknown variances before and after change are dynamically estimated
#         by using a combination of a growing window and a fixed-size sliding test window (size L)
#         essentially, the test decides whether the variances in the growing and in the fixed-size window are different
#         by comparing the log-likelihood ratio with a threshold h.  

#         detection: search starts with the upper bound k of the sliding window
#                    located at k = previous_change_time + 2*L. Thus at least L
#                    samples are available for parameter estimation in both the sliding and
#                    growing test window, respectively

#         change time estimation: each time a new event has been detected (alarm time ta), the maximum
#                    likelihood estimate t0 of the unknown change time is computed across
#                    all samples j = previous_change_time + L ... ta. The unknown variances before
#                    and after the change are estimated from intervals [previous_change_time ... j-1], and
#                    [j ... ta + Delta], respectively

#         the procedure is repeated with the previous change time being replaced by the new change time until
#         the end of the sequence is reached. If the parameter "mode" equals 'single', detection is terminated after the first event has been detected.
#         This option is useful, if the signals definitely contains a single change event only.

#         Detection is inhibited for the initial and last L samples of the sequence in order to avoid erroneous detections due to filter artifacts.
#         Therefore, changes can be detected only, if they are located in the interval 2*L+1 ... K-L-Delta, with K denoting the length of the input vector y 

# ------------------------------------------------------------------------------------------------------------

# tuning of parameters:

# the size L of the sliding test window determines the minimum distance of subsequent changes that can be detected:

# => select L as large as possible (in order to obtain reliable variance estimates
#    after change), but smaller than the shortest stationary epoch (i.e., epoch with constant variance) to be detected.

# the threshold h represents a tradeoff between nondetection of small events (large h) and false alarms (small h):

# => choose a value h as small as possible which still produces a tolerable rate of false alarms
#    if saglrstepvar is used together with a post processor (postproc.m), a
#    smaller threshold h can be used since events indicating transitions
#    with nonsignificant changes in variance will be eliminated by the post processor

# the parameter Delta confines parameter estimation of the ML change time estimation
# procedure a f t e r change to a minimum number of Delta samples.

# => choose Delta such that ta+Delta still will be located within the stationary epoch indicated by
#    the current alarm time ta. This parameter is not very critical.
#    Usually, a small number of samples (e.g, Delta=10) will do

# Version 2.5   by Gerhard.Staude@unibw-muenchen.de
# May 2010
  DeadZone = L # dead zones at beginning and end of sequence
  K = len(y) # length of sequence
  y_tmp = [x**2 for x in y]
  Sy = np.cumsum(y_tmp) # compute cumulative sum of squared data points
  
  # initialize variables
  PreviousChange = DeadZone+1 # preset previously detected change time (skip DeadZone samples at the beginning of the sequence)
  ta = np.array([])                     # alarm times
  t0 = np.array([])                     # change times
  
  ga = np.full(np.size(y),np.nan)    # test function for determination of alarm times
  g0 = np.full(np.size(y),np.nan)    # likelihood function for determination of change times
  
  k = DeadZone + 2*L + 1          # preset time index (upper bound of sliding test window)
                                    # such that at least L samples are available for estimating the
                                    # unknown variances before and after change, respectively
                                    # Note that DeadZone samples at the beginning and the end of the sequence
                                    # are omitted in order to avoid erroneous detections due to filter artifacts
                          
  # detection loop 
  while k <= K-DeadZone:
     
    # estimate variances
    theta_b = (Sy[k-L-1]-Sy[PreviousChange-1])/(k-L-PreviousChange) # variance before change at k-L (growing window)
    theta_a = (Sy[k-1]-Sy[k-L-1])/L                                 # variance after change at k-L (sliding window)
    theta_0 = (Sy[k-1]-Sy[PreviousChange-1])/(k-PreviousChange)     # variance in case of no change (total window)
      
    # compute log-likelihood ratio
    ga[k-1] = -0.5*( (k-L-PreviousChange)*np.log(theta_b)+L*np.log(theta_a)-(k-PreviousChange)*np.log(theta_0) )
       
    # stopping rule
    # (Note: stop is delayed by Delta samples to obtain several values 
    # of the test function after the alarm time for graphics)
    if ga[k-Delta-1]>=h:  # case of event detected:
        
      # update vector of alarm time(s)
      ta = np.append(ta,k-Delta)   
        
      # compute likelihood function of current change time
      j = np.array(range(PreviousChange+L,k-Delta+1)) # change time candidates
      theta_b = (Sy[j-1]-Sy[PreviousChange-1])/(j-PreviousChange)   # variance before change at j
      theta_a = (Sy[k-1]-Sy[j-1])/(k-j)                             # variance after change at j
        
      g0[j-1] = -0.5*( np.multiply((j-PreviousChange),np.log(theta_b))+np.multiply((k-j),np.log(theta_a)) ) 
      # likelihood function
        
      # determine maximum likelihood estimate of change time
      idx_tmp = np.where(g0[j-1]==np.max(g0[j-1]))
      CurrentChange = j[idx_tmp[0][0]-1]  # determine index of current maximum in g0
      t0 = np.append(t0,CurrentChange)
        
      g0[j-1] = g0[j-1] - np.max(g0[j-1])   # subtract maximum from likelihood function for more homogenius plots
        
      # initialize next search (dead zone: 2*L samples after previous change)
      PreviousChange = CurrentChange
      if mode == 'multiple':
        k = PreviousChange + 2*L - 1
      else:
        k = K  # exit loop in case of mode 'single'
     
    k = k + 1 # increment time index

  t0 = t0.astype(np.int64)
  ta = ta.astype(np.int64)
  return (t0,ta,g0,ga)