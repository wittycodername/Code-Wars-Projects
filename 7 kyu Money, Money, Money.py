
# 7 kyu Money, Money, Money

def calculate_years(principal, interest, tax, desired):
   y=0
   if principal >= desired:
      return 0
   else:
        while  principal < desired:
      
           y = y + 1
           principal = principal*(1+interest) - principal*interest*tax
           if principal >= desired:
              return y
   

   raise NotImplementedError("TODO: calculate_years")