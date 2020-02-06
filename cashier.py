def main():
        item = ""
        listItem=[]
        while item!="done" or item!="DONE":
                item = input("Item (enter \"done\" when finished): ")
                if item=="done" or item=="DONE":
                        break
                price = float(input ("Price: "))
                quentity = int(input ("Quentity: "))
                listItem.append({"name":item , "price":price , "quentity":quentity})

        print("\n--------------------\nreceipt \n--------------------")
        total=0
        for n in listItem:
                p=n["quentity"]*n["price"]
                total+=p
                print(str(n["quentity"])+" "+n["name"]+" "+str(p)+"KD")
        print("--------------------")
        print(f"Total Price: {total}KD")

        print (listItem)

	# write code here

if __name__ == '__main__':
	main()
