# Group3 - Gordon Stevens (300864022), Alejandro Zheng Zheng (301083081), Trevor Williamson (822916995), Tale Abor-Gabriel (301071358)

#######
# Import
#####
from random import uniform

#######
# generator : can be called continuously and get a pattern of numbers over a cycle
#             generates indoor temperatures, cold in the morning, heats right up in afternoon,
#             drops off at night.
#####
class generator:

   def __init__(self, period=24, jitter=0.25, y_min=17.0, y_max=22.0, round_digits=3):
      self.period = period # Number of periods
      self.counter = 0  # Number of values generated
      self.jitter = jitter # how much variation is wanted
      self.y_min = y_min
      self.y_max = y_max
      self.round_digits = round_digits
      # Ensure intervals are spread along the period
      self.step_interval_loci = [
         round(self.period * 0.10,0),
         round(self.period * 0.35,0),
         round(self.period * 0.55,0),
         round(self.period * 0.75,0),
         round(self.period * 0.90,0)]
      self.step_interval_adj_low = [
         1.11,
         1.99,
         2.33,
         1.99,
         1.11]
      self.step_interval_adj_high = [
         self.step_interval_adj_low[0]+self.jitter,
         self.step_interval_adj_low[1]+self.jitter,
         self.step_interval_adj_low[2]+self.jitter,
         self.step_interval_adj_low[3]+self.jitter,
         self.step_interval_adj_low[4]+self.jitter]
      #print(self.step_interval_loci)

   def __update_counter(self):
      self.counter += 1
      # Once the period has completed, reset the counter
      if self.counter >= self.period:
         self.counter = 0

   def __point_value(self):
      # Check the counter to see which interval this point is in
      if self.counter < self.step_interval_loci[0]:
         return self.y_min + uniform(self.step_interval_adj_low[0],self.step_interval_adj_high[0])

      elif self.counter < self.step_interval_loci[1]:
         return self.y_min + uniform(self.step_interval_adj_low[1],self.step_interval_adj_high[1])

      elif self.counter < self.step_interval_loci[2]:
         return self.y_min + uniform(self.step_interval_adj_low[2],self.step_interval_adj_high[2])

      elif self.counter < self.step_interval_loci[3]:
         return self.y_min + uniform(self.step_interval_adj_low[3],self.step_interval_adj_high[3])

      else:
         return self.y_min + uniform(self.step_interval_adj_low[4],self.step_interval_adj_high[4])

   @property
   def data(self):
      self.__update_counter()
      return round(self.__point_value(), self.round_digits)

#######
# Test Harness
#####

#gen = generator()

#x_values = 24
#a = 0
#x = [a + 1 for a in range(x_values)]
#y = [gen.data for _ in range(x_values)]

#import matplotlib.pyplot as plt
#plt.plot(x, y)
