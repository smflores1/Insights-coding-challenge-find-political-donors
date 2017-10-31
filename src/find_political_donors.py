import sys
import time
import datetime
import statistics as st

#The following function rounds x to the nearest integer, rounding all half-integers up:
def my_round(x):
    
    y = round(x)
    if x == y + 0.5:
        y += 1
    return y

#The following function checks that the input string has the structure of a zip code:
def check_zip_code_format(string):
    
    if len(string) != 5:
        return False
    
    for i in string:
        try:
            int(string)
        except ValueError:
            return False

    return True

#The following function checks that the input string is a valid date in years 2010-2018:
def check_date_format(string): 
    
    list_of_valid_dates = []
    
    for year in range(2010, 2019):
        for month in range(1, 13):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                month_length = 32
            elif month in [4, 6, 9, 11]:
                month_length = 31
            else:
                month_length = 29
            for day in range(1, month_length):
                list_of_valid_dates.append('0' * (2 - len(str(month))) + str(month) + '0' * (2 - len(str(day))) + str(day) + str(year))

    #Include two leap years:
    list_of_valid_dates += ['02292012', '02292016']
                
    if string in list_of_valid_dates:
        return True
    else:
        return False

#Main body:

start_time = time.time()

with open(sys.argv[1]) as in_file, open(sys.argv[2], 'w+') as out_file_zip, open(sys.argv[3], 'w+') as out_file_date:
    
    stream_dic = {}

    for line in in_file:
        
        broken_line = line.split('|')
        if len(broken_line) != 21:
            continue
            
        cmte_id = broken_line[0] #recipient id
        zip_code = broken_line[10][:5] #zip code
        transaction_dt = broken_line[13] #donation date
        transaction_amt = broken_line[14] #donation amount
        other_id = broken_line[15]
        
        #Ignore the line if other_id is empty:
        if cmte_id == '' or transaction_amt == '' or other_id != '':
            continue 
        
        #If the recipient id is not a key, create a new key, empty-value pair:
        #Each value will eventually be a list of two dictionaries. 
            #-The first dictionary contains donation-zip-code, donation-amount-list key, value pairs:
            #-The secon ddictionary contains donation-date, donation-amount-list key-value paris:
        if cmte_id not in stream_dic.keys():
            stream_dic[cmte_id] = [{}, {}]
        
        #Add the donation amount to the first dictionary of stream_dic[cmte_id]:
        if check_zip_code_format(zip_code):
            if zip_code not in stream_dic[cmte_id][0].keys():
                stream_dic[cmte_id][0][zip_code] = []
            stream_dic[cmte_id][0][zip_code] += [float(transaction_amt)]

            #Print out to 'medianvals_by_zip.txt':
            donation_list = stream_dic[cmte_id][0][zip_code]
            out_file_zip.write('{}|{}|{}|{}|{}\n'.format(cmte_id, 
                                                        zip_code, 
                                                        my_round(st.median(donation_list)), 
                                                        len(donation_list), 
                                                        my_round(sum(donation_list))))
        
        #Add the donation amount to the second dictionary of stream_dic[cmte_id]:
        if check_date_format(transaction_dt):
            datestamp = datetime.datetime.strptime(transaction_dt, '%m%d%Y')
            if datestamp not in stream_dic[cmte_id][1].keys():
                stream_dic[cmte_id][1][datestamp] = []
            stream_dic[cmte_id][1][datestamp] += [float(transaction_amt)]
        

    
    #Print out to 'medianvals_by_date.txt':
    for recipient in sorted(stream_dic.keys()):
        for datestamp in sorted(stream_dic[recipient][1].keys()):
            donation_list = stream_dic[recipient][1][datestamp]
            out_file_date.write('{}|{}|{}|{}|{}\n'.format(recipient, 
                                                         datestamp.strftime('%m%d%Y'), 
                                                         my_round(st.median(donation_list)), 
                                                         len(donation_list), 
                                                         my_round(sum(donation_list))))

print("Time to process the input file: --- %s seconds ---" % (time.time() - start_time))