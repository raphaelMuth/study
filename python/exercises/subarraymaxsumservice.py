import pprint

class SubArrayMaxSumService:
 
    def solution_one(self, arr):
        total_len = len(arr)
        actual_size = 1
        my_dict = {}
        while actual_size <= total_len:
            my_dict[actual_size] = { "elements": [], "max": [], "max_val": None }

            init_index = 0
            while init_index < total_len:
                sub_array = arr[init_index:(init_index+actual_size)]
                sum_sub_array = sum(sub_array)
                if my_dict[actual_size]["max_val"] == None or sum_sub_array > my_dict[actual_size]["max_val"]:
                    my_dict[actual_size]["max_val"] = sum_sub_array
                    my_dict[actual_size]["max"] = sub_array

                my_dict[actual_size]["elements"].append(sub_array)
                init_index = init_index + 1
                
            actual_size = actual_size + 1

        key_with_max_value = max(my_dict, key=lambda x: my_dict[x]['max_val'])

        # pp = pprint.PrettyPrinter(indent=4) 
        # pp.pprint(my_dict)
        
        return my_dict[key_with_max_value]['max']

    def solution_two(self, arr):
        total_len = len(arr)
        actual_size = 1
        max_sum_array = []
        while actual_size <= total_len:
            init_index = 0
            while init_index < total_len:
                sub_array = arr[init_index:(init_index+actual_size)]
                if len(max_sum_array) == 0 or sum(sub_array) > sum(max_sum_array):
                    max_sum_array = sub_array 
                init_index = init_index + 1
            actual_size = actual_size + 1
        return max_sum_array
