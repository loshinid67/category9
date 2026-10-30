# Bayesian Reasoning

disease = 0.01
positive = 0.90
false_positive = 0.05

not_disease = 1 - disease

p_positive = (positive * disease) + (false_positive * not_disease)

result = (positive * disease) / p_positive

print("Probability of Disease:",
      round(result * 100, 2), "%")
