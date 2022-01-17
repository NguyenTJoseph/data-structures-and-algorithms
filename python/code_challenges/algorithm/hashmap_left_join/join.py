
def left_join(ht1, ht2):
    output = []
    for index in ht1.buckets:
        if index:
            keys = list(index.value.keys())
            output.append([keys[0], index.value[keys[0]]])
    for index in ht2.buckets:
        status = False
        if index:
            keys = list(index.value.keys())
            for key_ in output:
                if keys[0] in key_:
                    key_.append(index.value[keys[0]])
                    status = True
            if status == False:
                output.append([keys[0], index.value[keys[0]]])
            

    return output





