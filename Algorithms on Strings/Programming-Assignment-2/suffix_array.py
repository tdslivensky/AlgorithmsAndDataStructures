# python3
import sys


def build_suffix_array(text):
    s = {}
    for i in range(len(text)):
        s[text[i:]] = i
    
    sPrime = sorted(s)
    result = []
    for item in sPrime:
        result.append(s[item])
    return result



if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))

# if __name__ == '__main__':
#   text = 'GAC$'
#   text = 'GAGAGAGA$'
#   text  = 'AACGATAGCGGTAGA$'
#   print(" ".join(map(str, build_suffix_array(text))))
