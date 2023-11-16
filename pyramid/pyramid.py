def decode(message_file) :
    file = open(message_file, 'r')
    lines = [line.strip() for line in file]
    lines.sort()
    pyramid = []
    layerWidth = 1
    end = False
    i = 0
    while not end:
        layer = []
        for num in range(layerWidth):
            layer.append(lines[i])
            i += 1
            if i == len(lines):
                end = True
                break
        pyramid.append(layer)
        layerWidth += 1
    ans = []
    for line in pyramid:
        ans.append(line[-1].split()[-1])
    return ' '.join(ans)

if __name__ == '__main__':
    print(decode("message2.txt"))