st = 'Print only the words that start with s in this sentence'

lst = st.split(' ')

s_guys = [word for word in lst if word[0] == 's']

print s_guys

numbs = [ number for number in range(0, 10) if number % 2 == 0 ]

print numbs

numb = [ number for number in range(1, 50) if number % 3 == 0 ]

print numb

stat = 'Print every word in this sentence that has an even number of letters'

check = stat.split()
for word in check:
    if len(word) % 2 == 0:
        print 'Even!!'

for integer in range(1, 100):
    print integer
    if integer % 3 == 0:
        print 'Fizz'
    if integer % 5 == 0:
        print 'FizzBuzz'


stunt = 'Create a list of the first letters of every word in this string'
mine = stunt.split(' ')










