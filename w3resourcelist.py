# def sum_list(items):
#     sum=1
#     for x in items:
#         sum=sum*x
#     return sum
# print(sum_list([1,2,3,5]))

# max number in a list
import logging

logging.basicConfig(filename='msg.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')
def maxnum(items):
    # print(items)
    logging.warning('%s User entered list values are',items)
    max1=items[0]
    logging.warning('Putting default value to 0')
    for a in items:
        if a > max1:
            max1=a
    return max1
    print(max1)

print(maxnum([9,6,5,3,4,10]))
res=maxnum([9,6,5,3,4,10])
logging.warning('%s is the max value from the list provided',format(res))





