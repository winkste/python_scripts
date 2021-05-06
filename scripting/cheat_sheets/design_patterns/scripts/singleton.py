# This cheat sheet demonstrates two variants to implement a singleton 
# class object in python. 

# Usage of a static method to generate the singleton and distribute it
#%%
class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

#%% 
# Variant two is working with an inner class to generate the 
# singleton object. Only the internal class object is the 
# singleton here, the wrapper class objects are still different

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        print('get_attrib')
        return getattr(self.instance, name)
    
    def __str__(self):
        print('str')
        return str(self.instance)
    
x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print(z)
print(x)
print(y)
print(repr(x))
print(repr(y))
print(repr(z))
# %%
