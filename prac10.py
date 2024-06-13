def build_info(first,last,**user_info):
 profile={"first":first,"last":last}
 for key,value in user_info.items():
  profile[key]=value
 return profile

user=build_info('deekshay',"jd",location="sakleshpur")
print(user)















def calling(names):
 for name in names:
  print("hi"+name)

names=["deekshay","akshay"]
calling(names)




def get_full_name(first, last):
 """Return a neatly formatted full name."""
 full_name = first + ' ' + last
 return full_name
musician = get_full_name('jimi', 'hendrix')
print(musician)


