#regular expressions
import re

from numpy.lib.function_base import average
result = re.match('Analytics',r'Analytics Vidhya is a popular data science community in India')
print(result)
#match for popular will return None since it is not occurring at the beginning of the sentence
result1 = re.match('popular',r'Analytics Vidhya is a popular data science community in India')
print(result1)

#search function looks for occurance anywhere in the search text
result2 = re.search('data',r'Analytics Vidhya is a popular data science community in India')
print(result2)
#use group() function to get the matched expressed
print(result2.group())

#findall returns all occurances of the pattern. It returns list object by default.
#findall is recommended always
result3 = re.findall('data',r'Analytics Vidhya is a popular data science community for data scientists in India')
print(result3)

#\b returns a match where the specified pattern occurs at the end of a word
str = r'Analytics Vidhya is the largest Analytics community of India'
x= re.findall(r'ics\b',str)
print(x)

#\d returns a match when the string contains numbers [o-9]
str = '2 million visits in Jan 2021'
x = re.findall('\d',str)
print(x)
if(x):
    print('Yes atleast one match')
else:
    print('No match')    

#adding + after \d will continue to extract digits till it encounters space 
y = re.findall('\d+',str)
print(y)

#use capital D to get matches that does not contain any digits
z = re.findall('\D+', str)
print(z)

#\w is for alpha-numeric match
#\W (capital W) is for non alpha-numeric

#metacharacters - these are nothing but characters with special meaning
str = 'Rohit and Rohan recently published a white paper'
#dot . indicates number of characters followed after Ro
x = re.findall('Ro.',str)
print(x)
x = re.findall('Ro...',str)
print(x)

#^ metacharacter is for string starting with the given expression
str = 'Data Science'
x = re.findall('^Data',str)
print(x)

#$ metacharacter checks if string ends with the given expression.
x = re.findall('Science$', str)
print(x)

str = 'easy easssy eay ey'
#check if the string contains 'ea' followed by 0 or more 's' character, and ending with y
x = re.findall('eas*y',str)
print(x)

#check if the string contains 'ea' followed by 1 or more 's' character, and ending with y
x = re.findall('eas+y',str)
print(x)

#check if the string contains 'ea' followed by 0 or 1 's' character, and ending with y
x = re.findall('eas?y',str)
print(x)

#pipe | metacharacter checks and returns if either of the word is present.
str = r'Analytics Vidhya is the largest data Analytics community of India'
x = re.findall('data|India', str)
print(x)

# A set of a bunch of characters inside []
str = r'Analytics Vidhya is the largest data Analytics community of India'
#check for characters y or d or h
x = re.findall('[ydh]', str)
print(x)

str = r'Analytics Vidhya is the largest data Analytics community of India'
#check for characters in the range a to g
x = re.findall('[a-g]', str)
print(x)

#example
str = r'Mars average distance from the Sun is roughtly 230 million km and its orbital period is 687 (Earth) days.'
#extract the numbers starting with 0 to 4
x = re.findall(r'[0-4]\d+', str)
print(x)

str = "@AV Largest Data Science Community #AV"
#extract all words that start with special character i.e. not alpha-numeric
x = re.findall("[^a-zA-Z0-9]\w+", str)
print(x)

str = 'Send an email to vasu@gmail.com, b.v@gmail.com, g_v@gmail.com for the meeting at 7 pm'
#extract the e-mail ids alone
#\w matches only alpha-numeric character, + repeats a character 1 or more times, 
x = re.findall('[a-zA-Z0-9._-]+@\w+\.com',str)
print(x)

#extract dates
text = 'London Olympic 2012 was held from 2012-07-27 to 2012/08/12'
#. here means occurance of any character
x = re.findall('\d{4}.\d{2}.\d{2}', text)
print(x)

text = 'London Olympic 2012 was held from 27 Jul 2012 to 12 Aug 2012'
#. here means occurance of any character
x = re.findall('\d{2}.\w{3}.\d{4}', text)
print(x)

text = 'London Olympic 2012 was held from 27 July 2012 to 12 August 2012'
#. here means occurance of any character
#notice the range 3,10 for the month being used, to capture words ranging from 3 to 10 characters
x = re.findall('\d{2}.\w{3,10}.\d{4}', text)
print(x)


