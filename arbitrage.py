import copy
# class Node:
#     def __init__(self,currencies = dict(), links = None):
#         self.currencies = currencies
#         self.links = links
dict_list = []
def node_factory(current_dict,input_array):
    b = 0
    starting_country = input_array[0]
    second_country = input_array[1]
    fowards_exchange = float(input_array[2])
    backwards_exchange = 1/fowards_exchange
    if current_dict == None:                
        second_node = dict()
        second_node[starting_country] = backwards_exchange
        current_dict[second_country] = second_node
        first_node = dict()
        first_node[second_country] = fowards_exchange
        current_dict[starting_country] = first_node
    if starting_country in current_dict.keys():
        current_dict[starting_country][second_country]=fowards_exchange
    else:       
        first_node = dict()
        first_node[second_country] = fowards_exchange
        current_dict[starting_country] = first_node
    if second_country in current_dict.keys():        
        current_dict[second_country][starting_country]=backwards_exchange
    else:
        second_node = dict()
        second_node[starting_country] = backwards_exchange
        current_dict[second_country] = second_node

    # print('backwards exchange',current_dict[second_country]['links'][starting_country])
    # print('fowards exchange',current_dict[starting_country]['links'][second_country])
    return current_dict
    # current_dict[input_array[0]] = 
def make_nodes():
    f = open('exchangeRatesF2016.txt','r')
    lines = f.readlines()
    graph = dict()
    counter = 0
    amount =0
    for line in lines:
        if counter >4:
            if counter == 5:
                amount = int(line)
                # print('no of currencies',line)
            else:
                array = line.split()
                # print('input ',array)
                # print('line ',counter)
                if array!=[]:
                    graph = node_factory(graph,array)
        counter += 1
    return (graph,amount)
def print_x(graph):
    for val in graph.keys():
        print()
        print('key',val)
        print()        
        for key2, value in graph[val].items():
            print(key2,value)
def print_payload(payload_dict):
    counter =0
    for y in payload_dict:
        counter += 1
        print('no ',counter)
        print(y)
        # for x in y:
        #     print('payload',y[x]['payload'],'path',y[x]['path'])
# def recursive_traverse(start,currency_from,currency_to,payload,graph,path,return_dict,list_of_dicts,max_len):        
#     if len(path) >= max_len:
#         return list_of_dicts
#     if currency_to == start and len(path)>=2:
#         payload = payload*graph[currency_from][currency_to]
#         path.append(currency_from)
#         path.append(currency_to)
#         return_dict['payload'] = payload
#         return_dict['path'] = path
#         return return_dict
#     elif currency_to not in path:
#         exchange_rate = 0
#         if currency_to == None:
#             currency_to = next(iter(graph[currency_from]))
#         exchange_rate = graph[currency_from][currency_to]
#         payload = payload*exchange_rate
#         path.append(currency_from)
           
#         for countries in graph[currency_to]:            
#             return_dictionary = recursive_traverse(start,currency_to,countries,payload,graph,path,return_dict,list_of_dicts,max_len)
#             if return_dict != None and return_dict != {}:
#                 if not (return_dict in list_of_dicts):
#                     if return_dict['payload'] > 1000:
#                         list_of_dicts.append(return_dict)
#                 else:
#                     return
#                 path = [start]
#                 return_dict = dict()

# def non_recursive_traverse(start,graph, payload,max_val,path):
#     key = start
#     while len(path)<max_val:
#         for x in graph[key]:
#             if x not in path:
#                 path.append(x)
#                 key = x
#                 payload = payload*graph[key][x]
#             if x == start and len(path)>2:
# def small_recursion

# def start(graph,payload,max_len):
#     for country in graph:
#         for links in graph[country]:

# def traverse2(start,currency_from,payload,graph,path,max_val):    
#     if len(path) >= max_val:
#         return
#     val = graph[currency_from]      
#     for x in val:
#         if len(path) >2 and x == start:
#                 path.append(x)  
#                 exchange_rate = graph[currency_from][x]
#                 payload = payload*exchange_rate
#                 if payload > 1000:                    
#                     return_dict = dict()
#                     return_dict['payload'] = payload
#                     return_dict['path'] = path
#                     global dict_list                        
#                     if dict_list== []:
#                         dict_list.append(return_dict)
#                         return payload
#                     else:
#                         for y in dict_list:
#                             if payload == y['payload']:
#                                 break
#                             else:
#                                 dict_list.append(return_dict)
#                                 return payload
#                 return payload
#         if x not in path:
#             path.append(x) 
#             exchange_rate = graph[currency_from][x]
#             payload = payload*exchange_rate            
#             val = traverse2(start,x,payload,graph,path,max_val)
#             if val != None:
#                 payload = 1000
def recursion3(start,path, payload,currency_from,currency_to,results,graph):
    if len(path)>9:
        return results
    elif currency_to not in path or currency_to == start:        
        if currency_to == None:
            currency_to = next(iter(graph[currency_from]))  
        # if currency_from not in path:
        path.append(currency_to)       
        exchange_rate = graph[currency_from][currency_to]
        payload = payload*exchange_rate

        if currency_to == start and len(path)>3:
            exists = False
            for x in results:
                if x['path'] == path:
                    exists = True
            if not exists:
                arbitrage = dict()
                arbitrage['payload']=payload
                arbitrage['path']=path
                if payload >1000:
                    return copy.deepcopy(arbitrage)
                else:
                    return None
            else:
                return None
        for x in graph[currency_to]:         
            an_arbitrage = None
            if x not in path or x == start:
                an_arbitrage = recursion3(start,path,payload,currency_to,x,results,graph)
            if an_arbitrage != None or an_arbitrage != []:
                result_copy = copy.deepcopy(results)
                result_copy.append(copy.deepcopy(an_arbitrage))
                results=result_copy
            # return results

    
def find_paths(graph,payload,max_val):
    referenced_list = []
    potential_payloads = []
    path = []
    for country in graph:
            path = []
            new_graph = copy.deepcopy(graph)
            payloads = recursion3(country,[country],1000,country,None,[],graph)
    return payloads        

def main():    
    (graph,amount) =make_nodes()
    # print_x(graph)
    payloads = find_paths(graph,1000,amount)
    print(payloads)
    print_payload(payloads)
if __name__ == "__main__":
  main()