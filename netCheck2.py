class netCheck(object):
    # Define my global variables - Such as the pay rates/tax rates
    rtPayRate = 14.85
    otPayRate = 14.85 * 1.5
    fica = 0.062
    mFICA = 0.0145
    orSTax = 0.067435192
    orSDisable = 0.017
    fedTax = 0.0403
    
    # Define __init__ function with regular time and overtime hours as (x,y) arguments
    def __init__(self, rtHours, otHours):
        # Create our own copy of the input variables to be used and modified within the class
        self.rtHours = rtHours                              # Input x(rtHours)
        self.otHours = otHours                              # Input y(otHours)
    
    # Define our function for doing our calculations
    def checkCalc(self):
            
        # Let's turn our input clones into float values
        self.frtHours = float(self.rtHours)
        self.fotHours = float(self.otHours)
        # Here's where we find out the exact total of hours worked (OT and RT) - not sure why I put this here
        self.hoursTotal = self.frtHours + self.fotHours
        # Here's our gross pay calculations (OT and RT)
        self.grossRT = self.frtHours * self.rtPayRate
        self.grossOT = self.fotHours * self.otPayRate
        # Here's the total gross pay for this pay period
        self.grossTotal = self.grossRT + self.grossOT
        # Now we calculate our taxes and expenses taken from our paycheck
        self.sAmt = self.grossTotal * self.fica             # FICA(Social Security)
        self.medAmt = self.grossTotal * self.mFICA          # FICA(Medicare)
        self.orSTaxAmt = self.grossTotal * self.orSTax      # OR State Tax
        self.orDisAmt = self.hoursTotal * self.orSDisable   # OR Disability
        # Not sure if this belongs or not, but it's better to have more on my check than less
        self.fedAmt = self.grossTotal * self.fedTax         # Federal Taxes
        # Here's our final net amount. The amount that we really care about!
        self.netAmt = self.grossTotal - self.sAmt - self.medAmt - self.orSTaxAmt - self.orDisAmt - self.fedAmt
        
        # Series of returns, would like to learn a more efficient way for this
        #print "Your net pay for this period is $%s, and that's for a total of %s hours!" %(round(self.netAmt, 2), self.hoursTotal)
        #print "Fica took $%s, Medicare took $%s, Oregon took $%s and $%s for Disability, the feds took $%s" %(round(self.sAmt, 2), round(self.medAmt, 2), round(self.orSTaxAmt, 2), round(self.orDisAmt, 2), round(self.fedAmt, 2))
        #print "Your RT Gross was $%s, your OT Gross was $%s, your total combined Gross was $%s" %(round(self.grossRT, 2), round(self.grossOT, 2), round(self.grossTotal, 2))
        print  "Approximate check pay", " -"*20
        print "-"*20, "Net Pay: $", round(self.netAmt, 2), "-"*20
        print "-"*20, "Gross Pay: $", round(self.grossTotal, 2), "-"*20
        print "-"*20, "RT Gross: $", round(self.grossRT, 2), "-"*20
        print "-"*20, "OT Gross: $", round(self.grossOT, 2), "-"*20
        print  "Deductions/Taxes", " -"*20
        print "-"*20, "Social Security: $", round(self.sAmt, 2), "-"*20
        print "-"*20, "Medicare: $", round(self.medAmt, 2), "-"*20
        print "-"*20, "Oregon State Tax: $", round(self.orSTaxAmt, 2), "-"*20
        print "-"*20, "Oregon Disability: $", round(self.orDisAmt, 2), "-"*20
        print  "Not sure about the Federal Yet", " -"*20
        print "-"*20, "Federal Tax: $", round(self.fedAmt, 2), "-"*20
        print "-/"*10, "Created by: D-vid", "\-"*10
# I need to update the values of the class arguments outside of the class, within my program code. Maybe I should instead use the class to just define variables to be used, and save the class arguments for the amount of hours since those are not static variables.
# netCheck()

hoursVarRT = input("How many hours have you worked this week of regular time? ")
hoursVarOT = input("How many hours have you worked this week of over time? ")
checkVar = netCheck(hoursVarRT,hoursVarOT)
checkVar.checkCalc()