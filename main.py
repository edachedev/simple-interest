business_logo = """
                                                                                                                                      
                                          ,--.                                    ,--.                                            
                        ,--.   ,--. ,---. |  | ,---. ,---. ,--,--,--. ,---.     ,-'  '-. ,---.                                    
                        |  |.'.|  || .-. :|  || .--'| .-. ||        || .-. :    '-.  .-'| .-. |                                   
                        |   .'.   |\   --.|  |\ `--.' '-' '|  |  |  |\   --.      |  |  ' '-' '                                   
                        '--'   '--' `----'`--' `---' `---' `--`--`--' `----'      `--'   `---'                                    
                                                 ,---.                       ,--.                          ,--.                   
            ,--. ,--.,--.,--. ,---. ,--.,--./  .-'     ,--,--.,--,--,  ,-|  |     ,---.  ,---. ,--,--, |  |,---.              
             \  '  / |  ||  |(  .-' |  ||  ||  `-,    ' ,-.  ||      \' .-. |    (  .-' | .-. ||      \`-'(  .-'              
              \   '  '  ''  '.-'  `)'  ''  '|  .-'    \ '-'  ||  ||  |\ `-' |    .-'  `)' '-' '|  ||  |   .-'  `)             
            .-'  /    `----' `----'  `----' `--'       `--`--'`--''--' `---'     `----'  `---' `--''--'   `----'              
            `---'                                                                                                             
,--.          ,--.                               ,--.                    ,--.              ,--.          ,--.                 
`--',--,--, ,-'  '-. ,---. ,--.--. ,---.  ,---.,-'  '-.     ,---. ,--,--.|  | ,---.,--.,--.|  | ,--,--.,-'  '-. ,---. ,--.--. 
,--.|      \'-.  .-'| .-. :|  .--'| .-. :(  .-''-.  .-'    | .--'' ,-.  ||  || .--'|  ||  ||  |' ,-.  |'-.  .-'| .-. ||  .--' 
|  ||  ||  |  |  |  \   --.|  |   \   --..-'  `) |  |      \ `--.\ '-'  ||  |\ `--.'  ''  '|  |\ '-'  |  |  |  ' '-' '|  |    
`--'`--''--'  `--'   `----'`--'    `----'`----'  `--'       `---' `--`--'`--' `---' `----' `--' `--`--'  `--'   `---' `--'    
                                                                                                                                                                                
"""

print(business_logo)
principal = float(input("Enter the initial principal amount: "))
rate = float(input("Enter the interest rate (in decimal form): "))
time_periods = int(input("Enter the number of time periods elapsed: "))
frequency = int(input("Enter the number of times interest applied per time period: "))

# Calculate Simple Interest
simple_interest = principal * (1 + rate * time_periods)

# Calculate Compound Interest
compound_interest = principal * (1 + rate / frequency) ** (frequency * time_periods)

print(f"\nSimple Interest for {business_logo} is: ${simple_interest:.2f}")
print(f"Compound Interest for {business_logo} is: ${compound_interest:.2f}")
