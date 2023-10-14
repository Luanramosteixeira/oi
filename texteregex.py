import re

listaNums = []

for i in range(401):
    listaNums.append(i)

for i in listaNums:
    if i == 0:
        listaNums.remove(i)

texto = "Você se arrasta pelo chão e se vê no covil de uma tribo de TROGLODITAS. Ao engatinhar passando por eles, sua bainha bate em uma pedra. Teste sua Sorte. Se você tiver sorte, vá para 15. Se você não tiver sorte, vá para 395."

nums1 = nums2 = nums3 = []
indice = -1

if re.search("vá para", texto):
    nums1 = re.findall("vá para \d{1}\D\D", texto)
    for i in nums1:
        for j in i:
            if i == ".":
                print("Tem")
                nums1.remove(i)
    nums2 = re.findall("vá para \d{2}\D", texto)
    for i in nums2:
        for j in i:
            indice +=1
            if j == ".":
               str(nums2).replace(nums2[-1], "")
    nums3 = re.findall("vá para \d{3}", texto)
    for i in nums3:
        for j in i:
            if i == ".":
                nums3.remove(i)

print(nums1)
print(nums2)
print(nums3)