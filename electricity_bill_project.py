#  TL/kWh
INDUSTRY_SINGLE_TIME_ENERGY_FEE = 3.053828
INDUSTRY_DAY_TIME_PERIOD_ENERGY_FEE = 3.091833
INDUSTRY_PEAK_PERIOD_ENERGY_FEE = 4.909037 
INDUSTRY_NIGHT_PERIOD_ENERGY_FEE = 1.625171
INDUSTRY_UNIT_DISTRIBUTION_FEE = 0.647998
INDUSTRY_ECT_RATE = 1.00
INDUSTRY_VAT_RATE = 20.00
INDUSTRY_HIGH_ELECTRICITY_CONSUMPTION_LIMIT = 10000
INDUSTRY_HIGH_BILL_LIMIT = 100000

EXCEPT_INDUSTRY_ECT_RATE = 5

PUBLIC_AND_PRIVATE_AND_OTHER_LOW_TARIFF_DAILY_AVERAGE_UPPER_LIMIT = 30
PUBLIC_AND_PRIVATE_AND_OTHER_LOW_TARIFF_SINGLE_TIME_FEE = 1.912220
PUBLIC_AND_PRIVATE_AND_OTHER_DAYTIME_PERIOD_FEE = 2.858616
PUBLIC_AND_PRIVATE_AND_OTHER_PEAKTIME_PERIOD_FEE = 4.588843
PUBLIC_AND_PRIVATE_AND_OTHER_NIGHT_PERIOD_FEE = 1.481941
PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE = 0.878175
PUBLIC_AND_PRIVATE_AND_OTHER_VAT_RATE = 20

PUBLIC_AND_PRIVATE_AND_OTHER_HIGH_TARIFF_SINGLE_TIME_FEE = 2.828414


RESIDENTIAL_LOW_TARIFF_DAILY_AVERAGE_UPPER_LIMIT = 8
RESIDENTIAL_LOW_TARIFF_SINGLE_TIME_FEE = 0.482187
RESIDENTIAL_DAYTIME_PERIOD_FEE = 1.157700
RESIDENTIAL_PEAKTIME_PERIOD_FEE = 2.083645
RESIDENTIAL_NIGHT_PERIOD_FEE = 0.417225
RESIDENTIAL_UNIT_DISTRIBUTION_FEE = 0.858883
RESIDENTIAL_VAT_RATE = 10

RESIDENTIAL_HIGH_TARIFF_SINGLE_TIME_FEE = 1.132271


RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_SINGLE_TIME_FEE =0.061590
RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_UNIT_DISTRIBUTION_FEE = 0.582521
RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_VAT_RATE = 10

AGRICULTURAL_ACTIVITIES_SINGLE_TIME_FEE = 1.653096
AGRICULTURAL_ACTIVITIES_DAYTIME_PERIOD_FEE = 1.704822
AGRICULTURAL_ACTIVITIES_PEAK_PERIOD_FEE = 2.800325
AGRICULTURAL_ACTIVITIES_NIGHT_PERIOD_FEE = 0.771882
AGRICULTURAL_ACTIVITIES_UNIT_DISTRIBUTION_FEE = 0.721579
AGRICULTURAL_ACTIVITIES_VAT_RATE = 10

LIGHTNING_SINGLE_TIME_FEE = 2.595835
LIGHTNING_UNIT_DISTRIBUTION_FEE = 0.841099
LIGHTNING_VAT_RATE = 10

FREE_CONSUMER_LIMIT = 1000

total_electricity_consumption_fee_of_all_consumers = 0
total_electricity_consumption_amount_of_all_consumers = 0
total_electricity_consumption_amount_of_industry_consumers = 0
total_electricity_consumption_amount_of_public_and_private_and_other_consumers = 0
total_electricity_consumption_amount_of_residential_consumers = 0
total_electricity_consumption_amount_of_lightning_consumers = 0
total_electricity_consumption_amount_of_agricultural_consumers = 0
total_revenue_of_gdz = 0
total_revenue_of_municipality = 0
total_revenue_of_state = 0
total_consumer_count = 0
loss_despite_multi_time_consumer_count = 0
industry_consumer_count = 0
industry_high_consumption_consumer_count = 0
public_and_private_and_other_consumer_count = 0
residential_consumer_count = 0
residential_discount_consumer_count = 0
agricultural_consumer_count = 0
lightning_consumer_count = 0
residential_highest_daily_average_consumption_amount_consumers_daily_average_consumption = 0
residential_highest_daily_average_consumption_amount_consumers_bill = 0
public_and_private_and_other_multi_consumer_count = 0
public_and_private_and_other_single_consumer_count = 0
total_electricity_consumption_amount_of_public_and_private_and_other_multi_consumers = 0
total_electricity_consumption_amount_of_public_and_private_and_other_single_consumers = 0
total_industry_consumers_amount_high_electric_consumption_amount_or_bill = 0
other_than_residential_highest_total_bill = 0
total_num_of_days_public_multi = 0
total_num_of_days_public_single = 0

consumer_no = int(input("Enter your consumer no: "))
while consumer_no <=0:
    consumer_no = int(input("First consumers no can't be negative or 0 try again: "))

def get_num_greater(lowest_limit):
    number = int(input())
    while number < lowest_limit :
        number = int(input("Incorrect data entry , please try again: "))
    return number

def single_time_total_invoice_calculate(total_electricity_consumption_amount_this_period,single_time_energy_fee_, ect,unit_distribution_fee, vat):
    global total_single_time_invoice_amount_this_period
    total_single_time_invoice_amount_this_period = ((total_electricity_consumption_amount_this_period*single_time_energy_fee_)*(1 + (ect/100))+(total_electricity_consumption_amount_this_period*unit_distribution_fee))*(1+(vat/100))
    

def single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, single_time_energy_fee):
    global single_time_electricity_consumption_fee_in_this_period
    single_time_electricity_consumption_fee_in_this_period = total_electricity_consumption_amount_in_this_period*single_time_energy_fee
    

def single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, single_time_energy_fee, ect):
    global single_time_ect_amount_in_this_period
    single_time_ect_amount_in_this_period = (total_electricity_consumption_amount_in_this_period*single_time_energy_fee)*ect/100
    

def single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, single_time_energy_fee, ect, unit_distribution_fee, vat):
    global single_time_vat_amount_in_this_period
    single_time_vat_amount_in_this_period = ((total_electricity_consumption_amount_in_this_period*single_time_energy_fee)*(1 + (ect/100))+(total_electricity_consumption_amount_in_this_period*unit_distribution_fee))*(vat/100)
    

def multi_time_total_invoice_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, daytime_electricity_fee, total_peaktime_period_electricity_consumption_amount_in_this_period, peaktime_electricity_fee, total_night_period_electricity_consumption_amount_in_this_period, night_electricity_fee,  ect, unit_distribution_fee, vat):
    total_multi_time_invoice_without_taxes = (total_daytime_period_electricity_consumption_amount_in_this_period*daytime_electricity_fee) + (total_peaktime_period_electricity_consumption_amount_in_this_period*peaktime_electricity_fee) + (total_night_period_electricity_consumption_amount_in_this_period*night_electricity_fee)
    global total_multi_time_invoice_amount_this_period
    total_multi_time_invoice_amount_this_period = ((total_multi_time_invoice_without_taxes*(1+(ect/100)))+(total_electricity_consumption_amount_in_this_period*unit_distribution_fee))*(1+(vat/100))
    

def multi_time_electricity_consumption_fee_in_this_period_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, daytime_electricity_fee, total_peaktime_period_electricity_consumption_amount_in_this_period, peaktime_electricity_fee, total_night_period_electricity_consumption_amount_in_this_period, night_electricity_fee):
    global multi_time_electricity_consumption_fee_in_this_period
    multi_time_electricity_consumption_fee_in_this_period = (total_daytime_period_electricity_consumption_amount_in_this_period*daytime_electricity_fee) + (total_peaktime_period_electricity_consumption_amount_in_this_period*peaktime_electricity_fee) + (total_night_period_electricity_consumption_amount_in_this_period*night_electricity_fee)
    

def multi_time_ect_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, daytime_electricity_fee, total_peaktime_period_electricity_consumption_amount_in_this_period, peaktime_electricity_fee, total_night_period_electricity_consumption_amount_in_this_period, night_electricity_fee, ect):
    total_multi_time_invoice_without_taxes = (total_daytime_period_electricity_consumption_amount_in_this_period*daytime_electricity_fee) + (total_peaktime_period_electricity_consumption_amount_in_this_period*peaktime_electricity_fee) + (total_night_period_electricity_consumption_amount_in_this_period*night_electricity_fee)
    global multi_time_ect_amount_in_this_period
    multi_time_ect_amount_in_this_period = (total_multi_time_invoice_without_taxes*(ect/100))
    

def multi_time_vat_amount_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, daytime_electricity_fee, total_peaktime_period_electricity_consumption_amount_in_this_period, peaktime_electricity_fee, total_night_period_electricity_consumption_amount_in_this_period, night_electricity_fee,  ect, unit_distribution_fee, vat):
    total_multi_time_invoice_without_taxes = (total_daytime_period_electricity_consumption_amount_in_this_period*daytime_electricity_fee) + (total_peaktime_period_electricity_consumption_amount_in_this_period*peaktime_electricity_fee) + (total_night_period_electricity_consumption_amount_in_this_period*night_electricity_fee)
    global multi_time_vat_amount_in_this_period
    multi_time_vat_amount_in_this_period = ((total_multi_time_invoice_without_taxes*(1+(ect/100)))+(total_electricity_consumption_amount_in_this_period*unit_distribution_fee))*(vat/100)
    

def unit_distirbution_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, unit_distribution_fee):
    global unit_distirbution_fee_in_this_period
    unit_distirbution_fee_in_this_period = (total_electricity_consumption_amount_in_this_period*unit_distribution_fee)
    

while consumer_no != 0:
    
    total_single_time_invoice_amount_this_period = 0
    total_multi_time_invoice_amount_this_period = 0
    total_electricity_consumption_fee_in_this_period = 0
    total_bill_in_this_period = 0
    total_ect_in_this_period = 0
    total_vat_in_this_period = 0
    total_single_time_period_invoice = 0
    total_multi_time_period_invoice = 0
    single_time_electricity_consumption_fee_in_this_period = 0
    single_time_ect_amount_in_this_period = 0
    single_time_vat_amount_in_this_period = 0
    multi_time_ect_amount_in_this_period = 0
    multi_time_vat_amount_in_this_period = 0
    multi_time_electricity_consumption_fee_in_this_period = 0
    unit_distirbution_fee_in_this_period = 0
    free_consumer_electricity_consumption_amount_in_current_year = 0

    consumer_type = input("Enter your consumer type Industry/Public and Private Services Sector and Other/Residential/Agricultural Activities/Lighting (I/i/P/p/R/r/A/a/L/l): ")
    
    while consumer_type  not in ["I","i","P","p","R","r","A","a","L","l"]:
        consumer_type = input("Incorrect data entry please try one of these(I/i/P/p/R/r/A/a/L/l): ")


    print("Enter your previous daytime period meter value (integer): ",end="")

    previous_daytime_period_meter_value = get_num_greater(0)
    
    print("Enter your current daytime period meter value (integer): ",end='')
    
    current_daytime_period_meter_value = get_num_greater(previous_daytime_period_meter_value)

    print("Enter your previous peaktime period meter value (integer): ",end='')

    previous_peaktime_period_meter_value = get_num_greater(0)

    print("Enter your current peaktime period meter value (integer): ",end='')

    current_peaktime_period_meter_value = get_num_greater(previous_peaktime_period_meter_value)

    print("Enter your previous night period meter value (integer): ",end='')

    previous_night_period_meter_value = get_num_greater(0)

    print("Enter your current night period meter value (integer): ",end='')

    current_night_period_meter_value = get_num_greater(previous_night_period_meter_value)
    
    print("Enter the number of days between previous and current meter reading dates (integer): ",end='')

    num_of_days_between_prev_and_current_meter_date = get_num_greater(0)

    print("Enter the total amount of electricity consumption in the current year until this period (integer): ",end='')

    total_amount_electric_consumption_current_year = get_num_greater(0)

    total_daytime_period_electricity_consumption_amount_in_this_period = current_daytime_period_meter_value - previous_daytime_period_meter_value
    total_peaktime_period_electricity_consumption_amount_in_this_period = current_peaktime_period_meter_value - previous_peaktime_period_meter_value
    total_night_period_electricity_consumption_amount_in_this_period = current_night_period_meter_value - previous_night_period_meter_value
    total_electricity_consumption_amount_in_this_period = total_daytime_period_electricity_consumption_amount_in_this_period + total_peaktime_period_electricity_consumption_amount_in_this_period + total_night_period_electricity_consumption_amount_in_this_period
    daily_average_electricity_consumption_amount = total_electricity_consumption_amount_in_this_period/num_of_days_between_prev_and_current_meter_date

    if total_amount_electric_consumption_current_year >= FREE_CONSUMER_LIMIT:
        deserve_free_customer = "You deserved to be a free customer!"
    else:
        deserve_free_customer = "You didn't deserve to be a free customer."

    if consumer_type != "L" and consumer_type !="l" and consumer_type !="R" and consumer_type !="r":
        preferred_tariff = input("Enter your preferred tariff Single-time/Multi-time (S/s/M/m): ")  
        while preferred_tariff != "S" and preferred_tariff !="s" and preferred_tariff !="M" and preferred_tariff !="m":
            preferred_tariff = input("Incorrect data entry please enter your preferred tariff (S/s/M/m): ")

    if consumer_type == "I" or consumer_type == "i":
        
        single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period,INDUSTRY_SINGLE_TIME_ENERGY_FEE,INDUSTRY_ECT_RATE,INDUSTRY_UNIT_DISTRIBUTION_FEE,INDUSTRY_VAT_RATE)
        single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, INDUSTRY_SINGLE_TIME_ENERGY_FEE, INDUSTRY_ECT_RATE)
        single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, INDUSTRY_SINGLE_TIME_ENERGY_FEE, INDUSTRY_ECT_RATE, INDUSTRY_UNIT_DISTRIBUTION_FEE, INDUSTRY_VAT_RATE)
        single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, INDUSTRY_SINGLE_TIME_ENERGY_FEE)

        multi_time_total_invoice_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, INDUSTRY_DAY_TIME_PERIOD_ENERGY_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, INDUSTRY_PEAK_PERIOD_ENERGY_FEE, total_night_period_electricity_consumption_amount_in_this_period, INDUSTRY_NIGHT_PERIOD_ENERGY_FEE, INDUSTRY_UNIT_DISTRIBUTION_FEE, INDUSTRY_ECT_RATE, INDUSTRY_VAT_RATE)
        multi_time_ect_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, INDUSTRY_DAY_TIME_PERIOD_ENERGY_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, INDUSTRY_PEAK_PERIOD_ENERGY_FEE, total_night_period_electricity_consumption_amount_in_this_period, INDUSTRY_NIGHT_PERIOD_ENERGY_FEE, INDUSTRY_ECT_RATE)
        multi_time_vat_amount_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, INDUSTRY_DAY_TIME_PERIOD_ENERGY_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, INDUSTRY_PEAK_PERIOD_ENERGY_FEE, total_night_period_electricity_consumption_amount_in_this_period, INDUSTRY_NIGHT_PERIOD_ENERGY_FEE, INDUSTRY_ECT_RATE, INDUSTRY_UNIT_DISTRIBUTION_FEE, INDUSTRY_VAT_RATE)
        unit_distirbution_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, INDUSTRY_UNIT_DISTRIBUTION_FEE)
        multi_time_electricity_consumption_fee_in_this_period_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, INDUSTRY_DAY_TIME_PERIOD_ENERGY_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, INDUSTRY_PEAK_PERIOD_ENERGY_FEE, total_night_period_electricity_consumption_amount_in_this_period, INDUSTRY_NIGHT_PERIOD_ENERGY_FEE)
        total_electricity_consumption_amount_of_industry_consumers += total_electricity_consumption_amount_in_this_period      
        industry_consumer_count += 1
        consumer_type_long = "Industry"
    
    elif consumer_type == "p" or consumer_type == "P":
        public_and_private_and_other_consumer_count += 1
        consumer_type_long = "Public and Private and Other"

        if daily_average_electricity_consumption_amount > PUBLIC_AND_PRIVATE_AND_OTHER_LOW_TARIFF_DAILY_AVERAGE_UPPER_LIMIT:
            single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period,PUBLIC_AND_PRIVATE_AND_OTHER_HIGH_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE, PUBLIC_AND_PRIVATE_AND_OTHER_VAT_RATE)
            single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_HIGH_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE)
            single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_HIGH_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE, PUBLIC_AND_PRIVATE_AND_OTHER_VAT_RATE)
            single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_HIGH_TARIFF_SINGLE_TIME_FEE)
        else: 
            single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period,PUBLIC_AND_PRIVATE_AND_OTHER_LOW_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE, PUBLIC_AND_PRIVATE_AND_OTHER_VAT_RATE)
            single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_LOW_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE)
            single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_LOW_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE, PUBLIC_AND_PRIVATE_AND_OTHER_VAT_RATE)
            single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_LOW_TARIFF_SINGLE_TIME_FEE)
        
        multi_time_total_invoice_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_NIGHT_PERIOD_FEE, PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE, EXCEPT_INDUSTRY_ECT_RATE, PUBLIC_AND_PRIVATE_AND_OTHER_VAT_RATE)
        multi_time_ect_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_NIGHT_PERIOD_FEE, EXCEPT_INDUSTRY_ECT_RATE)
        multi_time_vat_amount_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_NIGHT_PERIOD_FEE, EXCEPT_INDUSTRY_ECT_RATE, PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE, PUBLIC_AND_PRIVATE_AND_OTHER_VAT_RATE)
        unit_distirbution_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_UNIT_DISTRIBUTION_FEE)
        multi_time_electricity_consumption_fee_in_this_period_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_NIGHT_PERIOD_FEE)

        total_electricity_consumption_amount_of_public_and_private_and_other_consumers += total_electricity_consumption_amount_in_this_period
    
    elif consumer_type == "R" or consumer_type == "r":
        consumer_type_long = "Residential"
        residential_consumer_count +=1        
        total_electricity_consumption_amount_of_residential_consumers += total_electricity_consumption_amount_in_this_period
        
        residential_discount_consumer = input("Are you a family of the martyr or a veteran (y/Y/n/N): ")
        while residential_discount_consumer not in ["y","Y","n","N"]:
            residential_discount_consumer = input("Incorrect data entry please try again (y/Y/n/N): ")
        
        if residential_discount_consumer == "y" or residential_discount_consumer == "Y":
            residential_discount_consumer_count += 1

            single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period,RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_UNIT_DISTRIBUTION_FEE, RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_VAT_RATE)
            single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE)
            single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_UNIT_DISTRIBUTION_FEE, RESIDENTIAL_FAMILY_OF_MARTYRS_AND_VETERANS_VAT_RATE)
            single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, PUBLIC_AND_PRIVATE_AND_OTHER_HIGH_TARIFF_SINGLE_TIME_FEE)
            preferred_tariff = "s"    
        else:
            if daily_average_electricity_consumption_amount > RESIDENTIAL_LOW_TARIFF_DAILY_AVERAGE_UPPER_LIMIT:
            
                single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period,RESIDENTIAL_HIGH_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_UNIT_DISTRIBUTION_FEE, RESIDENTIAL_VAT_RATE)
                single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_HIGH_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE)
                single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_HIGH_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_UNIT_DISTRIBUTION_FEE, RESIDENTIAL_VAT_RATE)
                single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_HIGH_TARIFF_SINGLE_TIME_FEE)
            
            else: 
                single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_LOW_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_UNIT_DISTRIBUTION_FEE, RESIDENTIAL_VAT_RATE)
                single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_LOW_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE)
                single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_LOW_TARIFF_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_UNIT_DISTRIBUTION_FEE, RESIDENTIAL_VAT_RATE)
                single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_LOW_TARIFF_SINGLE_TIME_FEE)

            multi_time_total_invoice_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_NIGHT_PERIOD_FEE, RESIDENTIAL_UNIT_DISTRIBUTION_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_VAT_RATE)
            multi_time_ect_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_NIGHT_PERIOD_FEE, EXCEPT_INDUSTRY_ECT_RATE)
            multi_time_vat_amount_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_NIGHT_PERIOD_FEE, EXCEPT_INDUSTRY_ECT_RATE, RESIDENTIAL_UNIT_DISTRIBUTION_FEE, RESIDENTIAL_VAT_RATE)
            unit_distirbution_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, RESIDENTIAL_UNIT_DISTRIBUTION_FEE)
            multi_time_electricity_consumption_fee_in_this_period_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_PEAKTIME_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, RESIDENTIAL_NIGHT_PERIOD_FEE)
            
            preferred_tariff = input("Enter your preferred tariff Single-time/Multi-time (S/s/M/m): ")
            while preferred_tariff != "S" and preferred_tariff !="s" and preferred_tariff !="M" and preferred_tariff !="m":
                preferred_tariff = input("Incorrect data entry please enter your preferred tariff (S/s/M/m): ")

    elif consumer_type == "A" or consumer_type == "a":
        consumer_type_long = "Agricultural activities"
        agricultural_consumer_count += 1
        total_electricity_consumption_amount_of_agricultural_consumers += total_electricity_consumption_amount_in_this_period
        
        single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, AGRICULTURAL_ACTIVITIES_UNIT_DISTRIBUTION_FEE, AGRICULTURAL_ACTIVITIES_VAT_RATE)
        single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE)
        single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, AGRICULTURAL_ACTIVITIES_UNIT_DISTRIBUTION_FEE, AGRICULTURAL_ACTIVITIES_VAT_RATE)
        single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_SINGLE_TIME_FEE)

        multi_time_total_invoice_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_PEAK_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_NIGHT_PERIOD_FEE, AGRICULTURAL_ACTIVITIES_UNIT_DISTRIBUTION_FEE, EXCEPT_INDUSTRY_ECT_RATE, AGRICULTURAL_ACTIVITIES_VAT_RATE)
        multi_time_ect_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_PEAK_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_NIGHT_PERIOD_FEE, EXCEPT_INDUSTRY_ECT_RATE)
        multi_time_vat_amount_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_PEAK_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_NIGHT_PERIOD_FEE, EXCEPT_INDUSTRY_ECT_RATE, AGRICULTURAL_ACTIVITIES_UNIT_DISTRIBUTION_FEE, AGRICULTURAL_ACTIVITIES_VAT_RATE)
        unit_distirbution_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_UNIT_DISTRIBUTION_FEE)
        multi_time_electricity_consumption_fee_in_this_period_calculate(total_daytime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_DAYTIME_PERIOD_FEE, total_peaktime_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_PEAK_PERIOD_FEE, total_night_period_electricity_consumption_amount_in_this_period, AGRICULTURAL_ACTIVITIES_NIGHT_PERIOD_FEE)
    else:
        consumer_type_long = "Lightning"
        lightning_consumer_count += 1
        total_electricity_consumption_amount_of_lightning_consumers += total_electricity_consumption_amount_in_this_period
        
        single_time_total_invoice_calculate(total_electricity_consumption_amount_in_this_period,LIGHTNING_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, LIGHTNING_UNIT_DISTRIBUTION_FEE, LIGHTNING_VAT_RATE)
        single_time_ect_amount_calculate(total_electricity_consumption_amount_in_this_period, LIGHTNING_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE)
        single_time_vat_calculate(total_electricity_consumption_amount_in_this_period, LIGHTNING_SINGLE_TIME_FEE, EXCEPT_INDUSTRY_ECT_RATE, LIGHTNING_UNIT_DISTRIBUTION_FEE, LIGHTNING_VAT_RATE)
        single_time_electricity_consumption_fee_in_this_period_calculate(total_electricity_consumption_amount_in_this_period, LIGHTNING_SINGLE_TIME_FEE)
        preferred_tariff = "s"
    
    if preferred_tariff == "M" or preferred_tariff == "m":
        total_bill_in_this_period = total_multi_time_invoice_amount_this_period
        total_ect_in_this_period = multi_time_ect_amount_in_this_period
        total_vat_in_this_period = multi_time_vat_amount_in_this_period
        total_electricity_consumption_fee_in_this_period = multi_time_electricity_consumption_fee_in_this_period + unit_distirbution_fee_in_this_period
        other_tariffs_total_bill_in_this_period = total_single_time_invoice_amount_this_period
        profit_loss_amount = other_tariffs_total_bill_in_this_period - total_bill_in_this_period
        if consumer_type == "p" or consumer_type == "P":
            public_and_private_and_other_multi_consumer_count += 1 
            total_num_of_days_public_multi += num_of_days_between_prev_and_current_meter_date
            total_electricity_consumption_amount_of_public_and_private_and_other_multi_consumers += total_electricity_consumption_amount_in_this_period
        if profit_loss_amount < 0:
            loss_despite_multi_time_consumer_count +=1
        
    else :
        total_bill_in_this_period = total_single_time_invoice_amount_this_period
        total_ect_in_this_period = single_time_ect_amount_in_this_period
        total_vat_in_this_period = single_time_vat_amount_in_this_period
        total_electricity_consumption_fee_in_this_period = single_time_electricity_consumption_fee_in_this_period + unit_distirbution_fee_in_this_period
        other_tariffs_total_bill_in_this_period = total_multi_time_invoice_amount_this_period
        profit_loss_amount = other_tariffs_total_bill_in_this_period - total_bill_in_this_period
        if consumer_type == "p" or consumer_type == "P":
            public_and_private_and_other_single_consumer_count += 1 
            total_num_of_days_public_single += num_of_days_between_prev_and_current_meter_date
            total_electricity_consumption_amount_of_public_and_private_and_other_single_consumers += total_electricity_consumption_amount_in_this_period
    
    if consumer_type != "R" and consumer_type !="r" and total_bill_in_this_period > other_than_residential_highest_total_bill:
        other_than_residential_highest_total_bill = total_bill_in_this_period
        consumer_no_of_other_than_residential_highest_total_bill = consumer_no    
        other_than_residential_daily_average_electric_consumption_amunt = daily_average_electricity_consumption_amount
        other_than_residential_highest_total_bill_consumer_type = consumer_type

    if consumer_type == "r" or consumer_type == "R":    
        if daily_average_electricity_consumption_amount > residential_highest_daily_average_consumption_amount_consumers_daily_average_consumption:
            residential_highest_daily_average_consumption_amount_consumers_daily_average_consumption = daily_average_electricity_consumption_amount
            consumer_no_of_residential_highest_daily_average_consumption_amount = consumer_no
            residential_highest_daily_average_consumption_amount_consumers_bill = total_bill_in_this_period
    if consumer_type == "i" or consumer_type == "I" :
            if total_bill_in_this_period > INDUSTRY_HIGH_BILL_LIMIT or total_electricity_consumption_amount_in_this_period > INDUSTRY_HIGH_ELECTRICITY_CONSUMPTION_LIMIT:
                total_industry_consumers_amount_high_electric_consumption_amount_or_bill += 1


    total_revenue_of_gdz += total_electricity_consumption_fee_in_this_period
    total_revenue_of_municipality += total_ect_in_this_period
    total_revenue_of_state += total_vat_in_this_period
    total_electricity_consumption_fee_of_all_consumers += total_electricity_consumption_fee_in_this_period + unit_distirbution_fee_in_this_period
    total_electricity_consumption_amount_of_all_consumers += total_electricity_consumption_amount_in_this_period
    
    print(f"Your consumer no is: {consumer_no}")
    print(f"Your consumer type is: {consumer_type_long}")
    print(f"Your daytime period electricity consumption amount in this period is: {total_daytime_period_electricity_consumption_amount_in_this_period:.2f} kWh")
    print(f"Your peaktime period electricity consumption amount in this period is: {total_peaktime_period_electricity_consumption_amount_in_this_period:.2f} kWh")
    print(f"Your night period electricity consumption amount in this period is: {total_night_period_electricity_consumption_amount_in_this_period:.2f} kWh")
    print(f"Your total electricity consumption amount in this period is: {total_electricity_consumption_amount_in_this_period:.2f} kWh")
    print(f"Your total electricity consumption fee for this period : {total_electricity_consumption_fee_in_this_period:.2f} TL")
    print(f"Total ECT amount to be transferred to the municipality this period: {total_ect_in_this_period:.2f} TL")
    print(f"Total VAT amount to be transferred to the state this period: {total_vat_in_this_period:.2f} TL")
    print(f"Your total invoice amount for this period is: {total_bill_in_this_period:.2f} TL")
    print(f"Your profit/loss amount according to the other tariff is: {profit_loss_amount:.2f} TL")
    print(f"Your total electricity consumption amount in the current year is: {total_amount_electric_consumption_current_year:.2f}  kWh")
    print(deserve_free_customer)

    consumer_no = int(input("Enter your consumer no if there is no other consumer enter (0): "))
    while consumer_no < 0:
        consumer_no = int(input("Consumer no can't be negative try again: "))
total_consumer_count = industry_consumer_count + public_and_private_and_other_consumer_count + residential_consumer_count + agricultural_consumer_count + lightning_consumer_count

loss_despite_multi_time_consumer_percentage = (loss_despite_multi_time_consumer_count*100)/(total_consumer_count-residential_discount_consumer_count-lightning_consumer_count)
industry_consumer_percentage = (industry_consumer_count*100)/total_consumer_count        
industry_high_consumer_percentage = total_industry_consumers_amount_high_electric_consumption_amount_or_bill/industry_consumer_count
public_and_private_and_other_consumer_percentage = (public_and_private_and_other_consumer_count*100)/total_consumer_count
public_and_private_and_other_multi_consumer_percentage = (public_and_private_and_other_multi_consumer_count*100)/public_and_private_and_other_consumer_count
public_and_private_and_other_single_consumer_percentage = (public_and_private_and_other_single_consumer_count*100)/public_and_private_and_other_consumer_count
residential_consumer_percentage = (residential_consumer_count*100)/total_consumer_count
agricultural_act_consumer_percentage = (agricultural_consumer_count*100)/total_consumer_count
lightning_consumer_percentage = (lightning_consumer_count*100)/total_consumer_count


total_electricity_consumption_average_industry = (total_electricity_consumption_amount_of_industry_consumers)/industry_consumer_count
total_electricity_consumption_average_public_and_private_and_other_multi = (total_electricity_consumption_amount_of_public_and_private_and_other_multi_consumers)/(public_and_private_and_other_multi_consumer_count*total_num_of_days_public_multi)
total_electricity_consumption_average_public_and_private_and_other_single = (total_electricity_consumption_amount_of_public_and_private_and_other_single_consumers)/(public_and_private_and_other_single_consumer_count*total_num_of_days_public_single)
total_electricity_consumption_average_public_and_private_and_other = (total_electricity_consumption_amount_of_public_and_private_and_other_consumers)/public_and_private_and_other_consumer_count
total_electricity_consumption_average_residential = (total_electricity_consumption_amount_of_residential_consumers)/residential_consumer_count
total_electricity_consumption_average_agricultural_act = (total_electricity_consumption_amount_of_agricultural_consumers)/agricultural_consumer_count
total_electricity_consumption_average_lightning = (total_electricity_consumption_amount_of_lightning_consumers)/lightning_consumer_count

print(f"Industry type number of consumers and their percentage is: {industry_consumer_count}, %{industry_consumer_percentage}")
print(f"Industry type consumers average electricity consumption amounts in this period is: {total_electricity_consumption_average_industry} kWh")
print(f"Industry type consumers total electricity consumption amounts in this period: {total_electricity_consumption_amount_of_industry_consumers} kWh")
print(f"The number of industry type consumers whose electricity consumption amount is more than 10000 kWh or whose electricity bill is more than 100000 TL in the relevant period and their percentage among industry type consumers: {total_industry_consumers_amount_high_electric_consumption_amount_or_bill}, %{industry_high_consumer_percentage}")

print(f"Public and Private and other type number of consumers and their percentage is: {public_and_private_and_other_consumer_count}, %{public_and_private_and_other_consumer_percentage}")
print(f"Public and Private and other type consumers average electricity consumption amounts in this period is: {total_electricity_consumption_average_public_and_private_and_other} kWh")
print(f"Public and Private and other type consumers total electricity consumption amounts in this period: {total_electricity_consumption_amount_of_public_and_private_and_other_consumers} kWh")

print(f"Public and Private and other multi type number of consumers and their percentage among public and private and other consumers is: {public_and_private_and_other_multi_consumer_count}, %{public_and_private_and_other_multi_consumer_percentage}")
print(f"Public and Private and other multi type consumers average electricity consumption amounts in this period is: {total_electricity_consumption_average_public_and_private_and_other_multi} kWh")

print(f"Public and Private and other single type number of consumers and their percentage among public and private and other consumers is: {public_and_private_and_other_single_consumer_count}, %{public_and_private_and_other_single_consumer_percentage}")
print(f"Public and Private and other single type consumers average electricity consumption amounts in this period is: {total_electricity_consumption_average_public_and_private_and_other_single} kWh")


print(f"Residential type number of consumers and their percentage is: {residential_consumer_count}, %{residential_consumer_percentage}")
print(f"Residential type consumers average electricity consumption amounts in this period is: {total_electricity_consumption_average_residential} kWh")
print(f"Residential type consumers total electricity consumption amounts in this period: {total_electricity_consumption_amount_of_residential_consumers} kWh")
print(f"Consumer no of the residential type consumer with the highest daily average electricity consumption amount in the relevant period , this consumer's daily average electricity consumption amount (kWh) and total bill amount for this period (TL) : {consumer_no_of_residential_highest_daily_average_consumption_amount}, {residential_highest_daily_average_consumption_amount_consumers_daily_average_consumption} kWh, {residential_highest_daily_average_consumption_amount_consumers_bill} TL")

print(f"Agricultural Activities type number of consumers and their percentage is: {agricultural_consumer_count}, %{agricultural_act_consumer_percentage}")
print(f"Agricultural Activities type consumers average electricity consumption amounts in this period is: {total_electricity_consumption_average_agricultural_act} kWh")
print(f"Agricultural Activities type consumers total electricity consumption amounts in this period: {total_electricity_consumption_amount_of_agricultural_consumers} kWh")

print(f"Lightning type number of consumers and their percentage is: {lightning_consumer_count}, %{lightning_consumer_percentage}")
print(f"Lightning type consumers average electricity consumption amounts in this period is: {total_electricity_consumption_average_lightning} kWh")
print(f"Lightning type consumers total electricity consumption amounts in this period: {total_electricity_consumption_amount_of_lightning_consumers} kWh")

print(f"Consumer no of the consumer other than the residential type with the highest total bill amount in the relevant period, this consumer's consumer type, daily average electricity consumption amount (kWh) and total bill amount for this period (TL): {consumer_no_of_other_than_residential_highest_total_bill}, {other_than_residential_highest_total_bill_consumer_type}, {other_than_residential_daily_average_electric_consumption_amunt} kWh, {other_than_residential_highest_total_bill} TL")

print(f"Bornova's total electricity consumption amount in this period: {total_electricity_consumption_amount_of_all_consumers} kWh")

print(f"Total revenue amount obtained by the GDZ: {total_revenue_of_gdz} TL")
print(f"Total revenue amount obtained by the municipality: {total_revenue_of_municipality} TL")
print(f"Total revenue amount obtained by the state: {total_revenue_of_state} TL")

print(f"Among consumers other than residential (family of martyrs or veterans) type and lighting type, the percentage of those who made a loss despite choosing multi-time tariff in the relevant period: %{loss_despite_multi_time_consumer_percentage}")