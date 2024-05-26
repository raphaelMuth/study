import pprint

class SubArrayMaxSumService:
 
    def solve(self, arr):
        total_len = len(arr)
        actual_size = 1
        my_dict = {}
        while actual_size <= total_len:
            my_dict[actual_size] = { "elements": [], "max": [], "max_val": -1 }

            init_index = 0
            while init_index < total_len:
                sub_array = arr[init_index:(init_index+actual_size)]
                sum_sub_array = sum(sub_array)
                if sum_sub_array > my_dict[actual_size]["max_val"]:
                    my_dict[actual_size]["max_val"] = sum_sub_array
                    my_dict[actual_size]["max"] = sub_array

                my_dict[actual_size]["elements"].append(sub_array)
                init_index = init_index + 1
                
            actual_size = actual_size + 1

        key_with_max_value = max(my_dict, key=lambda x: my_dict[x]['max_val'])

        pp = pprint.PrettyPrinter(indent=4) 
        pp.pprint(my_dict)
        
        return my_dict[key_with_max_value]['max']

    def say_hello(self, name):
        return f"Hello, {name}!"