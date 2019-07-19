#A = 65, B = 66, …, Y = 89, Z = 90

#Write a program in which you print in capital letters when numbers are given

#Input format
#The first line is given a number of Ns to replace with alpha-bats. (1 ≤ N ≤ 1,000) The next line is given a space of N numbers. Each number is not less than 65, and is not greater than 90.

#output format
#The N number given in the first row is changed to alphabet and separated by spaces in order to print.

alphabet = {65:'A', 66:'B', 67:'C', 68:'D', 69:'E', 70:'F', 71:'G', 72:'H', 73:'I', 74:'J', 75:'K', 76:'L', 77:'M', 78:'N', 79:'O',80:'P', 81:'Q', 82:'R', 83:'S', 84:'T', 85:'U', 86:'V',87: 'W',88:'X', 89:'Y', 90:'Z'}

num=input()

str=input()


for i in str.split(' ') :
    print(alphabet[int(i)],' ' , end='' )



