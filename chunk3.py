def wrap(string,max_width):
    wrapped_string=""
    for i in range(0,len(string),max_width):
        wrapped_string+=string[i:i+max_width]+"\n"
    return wrapped_string






string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_width=4
wrpapped=wrap(string,max_width)
print(wrpapped)