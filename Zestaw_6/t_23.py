# interative solution was easier to me

def electrical_r(t, act):
    # 3 series and 3 parallel
    for i in range(0, len(t)):
        for j in range(i+1, len(t)):
            for z in range(j+1, len(t)):
                if act == (t[i] * t[j] * t[z])/((t[i] * t[j]) + (t[j] * t[z]) + (t[i] * t[z])) or act == t[i] + t[j] + t[z]:
                    return 1

            # 2 series then pararel on both
            for a in range(0, len(t)):
                if a!=i and a!=j and act == (t[a] * (t[i] + t[j]))/(t[i] + t[j] + t[a]) or act == (t[i] * t[j])/(t[i] + t[j]) + t[a]:
                    return 1








t = [1, 2, 3, 4, 5, 6]
a = 3.6
print(electrical_r(t, a))