    #Formatted Output and f-strings    
"""
    In this course we will use formatted output and f-string a lot, not just beautify the outputs but also generating some string arguments. 

    Let's create some variables:
"""
v1 = 5  # integer
v2 = 7.34  # float
v3 = "Cevdet"   # string
v4 = True   # bool
v5 = 2j     # complex 

"""
    We will use the format specifiers as:
        d: integers
        f,e,g: floating-point numbers
        b: binary numbers
        s: string 
"""

# Standard Concetration
print("v1 = ", v1, " | v2 = ", v2, " | v3 = ", v3, " | v4 = ", v4, " | v5 = ", v5)

# Legacy Formatting
print("v1 = %d | v2 = %f | v2 = %e | v2 = %g | v3 = %s | v4 = %s | v4 = %d | v5 = %s" % (v1, v2, v2, v2, v3, v4, v4, v5))

# Format Method of String Object
print("v1 = {0} | v2 = {1} | v3 = {2} | v4 = {3} | v5 = {4}".format(v1, v2, v3, v4, v5))

# f-strings
print(f"v1 = {v1} | v2 = {v2} | v3 = {v3} | v4 = {v4} | v5 = {v5}")

# f-strings with Specifiers
print(f"v1 = {v1:05d} | v1 = {v1:b} | v2 = {v2:12.3f} | v2 = {v2:12.3e} | v2 = {v2:6g}")