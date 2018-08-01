
import numpy as np
import DetectionEvalSourceCode as det
import startTimes as st
import countingOnsets as co
epsilon = np.finfo(float).eps

def get_F(training_set, threshold):
    num_onsets = 0
    true_pos = 0
    false_neg = 0
    false_pos = 0
    precision = []
    recall = []
    fmeasure = []

    for unit in training_set:
        start_times = st.get_start_time(unit)
        for start_time in start_times:
            Tp, Fp, Fn = det.threshold(unit, start_time, threshold)
#           find LOCAL num_onsets, true_pos, false_neg, false_pos
            num_onsets += co.counting_onsets(unit, start_time)
            true_pos += Tp
            false_neg += Fn
            false_pos += Fp
    if (true_pos + false_pos) == 0:
        P = 0.0
    else:
        P = true_pos / (true_pos + false_pos)
    if num_onsets == 0:
        R = 0.0
    else:
        R = true_pos / (true_pos + false_neg)
    if P<epsilon and R<epsilon:
        F = 0.0
    else:
        F = 2*P*R / (P+R)
        
    return F

