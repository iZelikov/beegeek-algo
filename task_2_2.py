def calculate(vars,values,exp):
    for var, value in zip(vars, values):
        exp = exp.replace(var,str(value))

    return eval(exp)

def is_function(pairs):
  return len(set(list(zip(*pairs))[0]))==len(pairs)