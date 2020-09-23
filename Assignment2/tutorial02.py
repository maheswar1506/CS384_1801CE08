from math import sqrt
# All decimal 3 places

# Function to compute mean
def mean(first_list):
    # mean Logic 
    summation_value = 0
    for item in first_list:
        if isinstance(item,(int,float)):
            summation_value = summation_value+item
        else:
            return 0
    mean_value = 0
    if len(first_list)>0:
        mean_value = summation_value/len(first_list)
    else:
        return 0
    return mean_value

# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    for item in first_list:
        if isinstance(item,(int,float)):
            pass
        else:
            return 0
    first_list = sorting(first_list)
    list_len = len(first_list)
    median_value = 0
    if list_len%2 == 0:
        median_value = (first_list[list_len//2]+first_list[(list_len//2)-1])/2
    else:
        median_value = first_list[(list_len//2)]
    return median_value

# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    standard_deviation_value = sqrt(variance(first_list))
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    for item in first_list:
        if isinstance(item,(int,float)):
            pass
        else:
            return 0
    xx_list = list()
    x_mean = mean(first_list)
    for i in range(len(first_list)):
        xx_list.append((first_list[i]-x_mean)**2)
    xx_sum = summation(xx_list)
    variance_value = 0
    if len(xx_list)>0:
        variance_value = xx_sum/len(first_list)
    else:
        return 0
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    for item in first_list:
        if isinstance(item,(int,float)):
            pass
        else:
            return 0
    for item in second_list:
        if isinstance(item,(int,float)):
            pass
        else:
            return 0
    rmse_value = sqrt(mse(first_list,second_list))
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    summation_value = 0
    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            if isinstance(first_list[i],(int,float)) and isinstance(second_list[i],(int,float)):
                summation_value = summation_value + ((first_list[i]-second_list[i])**2)
            else:
                return 0
    else:
        return 0
    mse_value = 0
    if len(first_list)>0:
        mse_value = summation_value/len(first_list)
    else:
        return 0
    return mse_value



# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    xy_list = list()
    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            if isinstance(first_list[i],(int,float)) and isinstance(second_list[i],(int,float)):
                xy_list.append(abs(first_list[i]-second_list[i]))
            else:
                return 0
    else:
        return 0
    mae_value = 0
    if len(first_list)>0:
        mae_value = summation(xy_list)/len(first_list)
    else:
        return 0
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    xy_list = list()
    xx_list = list()
    mean_value = mean(first_list)
    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            if isinstance(first_list[i],(int,float)) and isinstance(second_list[i],(int,float)):
                xy_list.append((first_list[i]-second_list[i]) ** 2)
                xx_list.append((first_list[i]-mean_value)**2)
            else:
                return 0
    else:
        return 0
    xy_sum = summation(xy_list)
    xx_sum = summation(xx_list)
    nse_value = 0
    if xx_sum != 0:
        nse_value = (1-(xy_sum/xx_sum))
    else:
        return 0
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    x_mean = mean(first_list)
    y_mean = mean(second_list)
    num = list()
    xx2_list = list()
    yy2_list = list()
    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            if isinstance(first_list[i],(int,float)) and isinstance(second_list[i],(int,float)):
                num.append((first_list[i]-x_mean)*(second_list[i]-y_mean))
                xx2_list.append((first_list[i]-x_mean)**2)
                yy2_list.append((second_list[i]-y_mean)**2)
            else:
                return 0

    else:
        return 0
    num_sum = summation(num)
    xx2_sum = summation(xx2_list)
    yy2_sum = summation(yy2_list)
    pcc_value = 0
    if xx2_sum==0 or yy2_sum==0:
        return 0
    else:
        pcc_value = num_sum/(sqrt(xx2_sum)*sqrt(yy2_sum))
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    for item in first_list:
        if isinstance(item,(int,float)):
            pass
        else:
            return 0
    x_mean = mean(first_list)
    xx_list = list()
    std_val = standard_deviation(first_list)
    for i in range(len(first_list)):
        if std_val !=0:
            xx_list.append(((first_list[i]-x_mean)/std_val)**3)
        else:
            return 0
    xx_sum = summation(xx_list)
    skewness_value = 0
    if len(first_list)>0:
        skewness_value = xx_sum/len(first_list)
    else:
        return 0
    return skewness_value
   
def sorting(first_list):
    # Sorting Logic
    sorted_list = first_list[:]
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list)-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j],sorted_list[j+1] = sorted_list[j+1],sorted_list[j]
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for item in first_list:
        if isinstance(item,(int,float)):
            summation_value = summation_value + item
        else:
            return 0
    return summation_value
