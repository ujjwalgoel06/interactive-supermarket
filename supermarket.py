def show_menu():
        print('--------------------------------------------------')
        print('--------------------------------------------------')
        print('                    MY BAZAAR                    ')
        print('--------------------------------------------------')
        print('--------------------------------------------------\n')
        print('Hello! Welcome to my grocery store!')
        print('Following are the products available in the shop:\n')
        print('--------------------------------------------------')
        print('CODE | DESCRIPTION |   CATEGORY   | COST (Rs)')
        print('--------------------------------------------------')
        print('  0  | Tshirt      | Apparels     | 500')
        print('  1  | Trousers    | Apparels     | 600')
        print('  2  | Scarf       | Apparels     | 250')
        print('  3  | Smartphone  | Electronics  | 20,000')
        print('  4  | iPad        | Electronics  | 30,000')
        print('  5  | Laptop      | Electronics  | 50,000')
        print('  6  | Eggs        | Eatables     | 5')
        print('  7  | Chocolate   | Eatables     | 10')
        print('  8  | Juice       | Eatables     | 100')
        print('  9  | Milk        | Eatables     | 45')
        print('--------------------------------------------------')


def get_regular_input():
        print('\n--------------------------------------------------')
        print('ENTER ITEMS YOU WISH TO BUY')
        print('--------------------------------------------------\n')
        x=input('Enter the item codes (space separated): ')
        if x=='':
                return [0,0,0,0,0,0,0,0,0,0]
        else:
                list1=x.split()
                list_int=['0','1','2','3','4','5','6','7','8','9']
                list2=[]
                list3=[]

                for i in list1:
                        k=False
                        for j in list_int:
                                if i==j:
                                        list2.append(int(i))
                                        k=True
                        if k==False:
                            print('INVALID ITEM CODE ',i)

                for i in range(10):
                        x=list2.count(i)
                        list3.append(x)

                return list3
	


def get_bulk_input():
        print('--------------------------------------------------')
        print('ENTER ITEMS AND QUANTITY')
        print('--------------------------------------------------')
        list2=[0,0,0,0,0,0,0,0,0,0]
        while True:
                x=input('\nEnter code and quantity (leave blank to stop): ')
                if x == ' ' or x=='':
                        break
                else:
                        list1=x.split()
                        list_int=['0','1','2','3','4','5','6','7','8','9']
                        list_item=['Tshirt','Trouseers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
                        y=list1[0]
                        z=int(list1[1])
                        t=int(y)
                        k=False
                        for j in list_int:
                                if y==j:
                                        if z>0:
                                                list2[t]+=z
                                                k=True
                                                print('You added ',list1[1],' ',list_item[int(j)])
                        if k==False:
                                print('Invalid code and quantity. Try again.')
                                
        print('Your order has been finalized.')

        return list2


def print_order_details(quantities):
        print('\n--------------------------------------------------')
        print('ORDER DETAILS                                     ')
        print('--------------------------------------------------\n')
        list_item=['Tshirt','Trousers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
        list_cost=[500,600,250,20000,30000,50000,5,10,100,45]
        count=1
        total_cost=0
        for i in range(10):
                if quantities[i]>=1:
                        item_cost=list_cost[i]*quantities[i]
                        total_cost+=item_cost
                        print('[',count,'] ',list_item[i],' X ',quantities[i],' = Rs',list_cost[i],' * ',quantities[i],' = Rs',item_cost)
                        count+=1
        print('\nTOTAL COST = ',total_cost)


def calculate_category_wise_cost(quantities):
        print('\n--------------------------------------------------')
        print('CATEGORY-WISE COST                                  ')
        print('--------------------------------------------------\n')
        list_cost=[500,600,250,20000,30000,50000,5,10,100,45]
        apparels_cost=0
        electronics_cost=0
        eatables_cost=0
        for i in range(3):
                if quantities[i]>=1:
                        apparels_cost+=list_cost[i]*quantities[i]
        for i in range(3,6):
                if quantities[i]>=1:
                        electronics_cost+=list_cost[i]*quantities[i]
        for i in range(6,10):
                if quantities[i]>=1:
                        eatables_cost+=list_cost[i]*quantities[i]
        category_cost=(apparels_cost,electronics_cost,eatables_cost)
        if apparels_cost>0:
                print('Apparels = Rs ',apparels_cost)
        if electronics_cost>0:
                print('Electronics = Rs ',electronics_cost)
        if eatables_cost>0:
                print('Eatables = Rs ',eatables_cost)
        return(category_cost)
                        


def get_discount(cost, discount_rate):
	
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
        print('\n--------------------------------------------------')
        print('DISCOUNTS')
        print('--------------------------------------------------\n')
        discounted_apparels_cost=apparels_cost
        discounted_electronics_cost=electronics_cost
        discounted_eatables_cost=eatables_cost
        discount1=0
        discount2=0
        discount3=0
        if apparels_cost>0 or electronics_cost>0 or eatables_cost>0:
                if apparels_cost>=2000:
                        discount1=get_discount(apparels_cost,10/100)
                        discounted_apparels_cost-=discount1
                        print('[Apparels] Rs',apparels_cost,' - Rs',discount1,' = Rs',discounted_apparels_cost)
                if electronics_cost>=25000:
                        discount2=get_discount(electronics_cost,10/100)
                        discounted_electronics_cost-=discount2
                        print('[Electronics] Rs',electronics_cost,' - Rs',discount2,' = Rs',discounted_electronics_cost)
                if eatables_cost>=500:
                        discount3=get_discount(eatables_cost,10/100)
                        discounted_eatables_cost-=discount3
                        print('[Eatables] Rs',eatables_cost,' - Rs',discount3,' = Rs',discounted_eatables_cost)
                if apparels_cost<2000 and electronics_cost<25000 and eatables_cost<500:
                        print('NO DISCOUNT APPLICABLE')
        print('\nTOTAL DISCOUNT = Rs',discount1+discount2+discount3)
        print('TOTAL COST = Rs ',discounted_apparels_cost+discounted_electronics_cost+discounted_eatables_cost)
        tup2=(discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost)
        return tup2


def get_tax(cost, tax):

	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
        print('\n--------------------------------------------------')
        print('TAX')
        print('--------------------------------------------------\n')
        tax_apparels_cost=0
        tax_electronics_cost=0
        tax_eatables_cost=0
        tax1=0
        tax2=0
        tax3=0
        if apparels_cost>0:
                tax1=get_tax(apparels_cost,10/100)
                tax_apparels_cost=apparels_cost+tax1
                print('[Apparels] Rs',apparels_cost,' * 0.10 = Rs',tax1)
        if electronics_cost>0:
                tax2=get_tax(electronics_cost,15/100)
                tax_electronics_cost=electronics_cost+tax2
                print('[Electronics] Rs',electronics_cost,' * 0.15 = Rs',tax2)
        if eatables_cost>0:
                tax3=get_tax(eatables_cost,5/100)
                tax_eatables_cost=eatables_cost+tax3
                print('[Eatables] Rs',eatables_cost,' * 0.05 = Rs',tax3)

        total_tax= tax1 + tax2 + tax3
        total_cost_including_tax=tax_apparels_cost + tax_electronics_cost + tax_eatables_cost
        tup3=(total_cost_including_tax,total_tax)
        print('\nTOTAL TAX = Rs',total_tax)
        print('TOTAL COST = Rs',total_cost_including_tax)
        return tup3
        


def apply_coupon_code(total_cost):
        print('\n--------------------------------------------------')
        print('COUPON CODE')
        print('--------------------------------------------------\n')
        total_cost_after_coupon_discount=total_cost
        total_coupon_discount=0
        k=True
        while k==True:
                x=input('Enter coupon code (Else leave blank) : ')
                if x==' ' or x=='':
                        print('NO COUPON CODE APPLIED\n')
                        print('TOTAL COUPON DISCOUNT = 0')
                        k=False
                elif x=='HELLE25':
                        if total_cost>=25000:
                                p=get_discount(total_cost,25/100)
                                if p>=5000:
                                        total_cost_after_coupon_discount-=5000
                                else:
                                       total_cost_after_coupon_discount-=p
                                total_coupon_discount=5000
                                print('[HELLE25] min(5000, Rs',total_cost,' * 0.25) = Rs 5000\n')
                                print('TOTAL COUPON DISCOUNT = Rs 5000')
                        else:
                                print('TOTAL COUPON DISCOUNT = 0')
                        k=False
                        
                elif x=='CHILL50':
                        if total_cost>=50000:
                                y=get_discount(total_cost,50/100)
                                if y>=10000:
                                        total_cost_after_coupon_discount-=10000
                                else:
                                       total_cost_after_coupon_discount-=y
                                total_coupon_discount=10000
                                print('[CHILL50] min(10000, Rs',total_cost,' * 0.50) = Rs 10000\n')
                                print('TOTAL COUPON DISCOUNT = Rs 10000')
                        else:
                                print('TOTAL COUPON DISCOUNT = 0')
                        k=False
                else:
                        print('Invalid coupon code. Try again.')
                
        print('TOTAL COST = ',total_cost_after_coupon_discount)
        tup4=(total_cost_after_coupon_discount, total_coupon_discount)
        return tup4


def main():
        show_menu()
        k=True
        while k==True:
                x=input('Would you like to buy in bulk (Y or y / N or n : )')
                if x!='Y' and x!='y' and x!='N' and x!='n'or x=='':
                        print('INVALID INPUT. Try again.')
                        k=True
                else:
                        if x =='Y' or x=='y':
                                quantities=get_bulk_input()
                        elif x =='N' or x=='n':
                                quantities=get_regular_input()
                        print_order_details(quantities)

                        category_wise_cost=calculate_category_wise_cost(quantities)
                        apparels_cost=category_wise_cost[0]
                        electronics_cost=category_wise_cost[1]
                        eatables_cost=category_wise_cost[2]
        
                        discounted_category_wise_cost=calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)
                        discounted_apparels_cost=discounted_category_wise_cost[0]
                        discounted_electronics_cost=discounted_category_wise_cost[1]
                        discounted_eatables_cost=discounted_category_wise_cost[2]

                        tax=calculate_tax(discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost)
                        total_cost=tax[0]
                        m=apply_coupon_code(total_cost) 
                        k=False
        print('\nThank you for visiting!')

	

if __name__ == '__main__':
	main()

