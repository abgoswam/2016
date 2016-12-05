import matplotlib.pyplot as plt

class Account:
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def get_balance(self):
        return self.balance

    def statement(self):
        print 'Balance:', self.balance

acct = Account(200)
print acct.get_balance()

df2 = pd.DataFrame({
    'A' : 1.,
    'B' : pd.Timestamp('20130102'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })

x = np.linspace(0, 10, 500)

# %%
x = 2 * x
plt.plot(x, np.sin(x))
plt.show()

#
string = 'hydrogentrials'
for index, letter in enumerate(string):
    print ((letter, index))

myname = "abhishek goswami"

#
print "aa"
print "bb"

# %%
print "cc"
print "dd"

df2.abs

df2.columns
