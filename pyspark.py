

# import pyspark 


# # Import SparkSession
# from pyspark.sql import SparkSession

# # Create SparkSession 
# spark = SparkSession.builder.appName("SparkByExamples.com").getOrCreate() 
#     #   .master("local[1]") \
   
      
# print('hello vs code world')


# data = [('James','','Smith','1991-04-01','M',3000),
#   ('Michael','Rose','','2000-05-19','M',4000),
#   ('Robert','','Williams','1978-09-05','M',4000),
#   ('Maria','Anne','Jones','1967-12-01','F',4000),
#   ('Jen','Mary','Brown','1980-02-17','F',-1)
# ]

# columns = ["firstname","middlename","lastname","dob","gender","salary"]
# df = spark.createDataFrame(data=data, schema = columns)

# df.show()

def swap_case(s):
    new_str = ""
    for i in range(len(s)):
        if s[i].isupper():
            new_str = new_str + s[i].lower()
        elif s[i].islower:
            new_str = new_str + s[i].upper()
        else:
            new_str = new_str + i     
    return new_str
print(swap_case('Hi Hello Im SIVA'))