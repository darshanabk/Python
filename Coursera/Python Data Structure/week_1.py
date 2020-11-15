text = "X-DSPAM-Confidence:    0.8475"
finding_ = text.find('0')
print(float(text[finding_:]))
