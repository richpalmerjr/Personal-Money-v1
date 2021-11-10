def convertToFloat(amt):
  z = amt.replace("$","")
  z = round(float(z.replace(",","")),2)
  return z
