'''
Copyright 2018 Christina Lee

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

#principal
P=0
#interest
I=0
#monthly withdrawal amt
MW=0

W=0
M=0
N=12

print ("Interest Calculator")
print ("This calculator calculates how long it will take to withdraw money from an account which receives a given amount of interest which is compounded monthly, and the remainder of money left over in the account after withdrawal.")
P=float(input("Enter the initial amount in the account"))
I=float(input("Enter the amount of annual interest"))
MW=float(input("Enter the monthly withdrawal amount"))

Pprev=P
P=P*(1 + I/N)
Imonth=P-Pprev
print("Interest in first month: " + str(Imonth))
print("Monthly Withdrawal amount: " + str(MW))
print("---------------------------------------")

if (Imonth < MW):

   M=M+1
   while (P > MW):
      P=P*(1 + I/N)-MW
      M=M + 1
      W=W + MW

   print ("Account balance at end of " + str(M) + " months: " + str(P))
   print ("Months passed: " + str(M))
   print ("Months of withdrawals passed: " + str(M-1))
   print ("Withdrawn amount: " +  str(W))
else:
    print ("First month of interest is greater than the monthly withdrawal amount.  You will never run out of money!")


   
   
