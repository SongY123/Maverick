class SymbolTable:
    
    def __init__(self):
        self.dic_list = [{}]
        self.cur_scope = 0

    def get_item(self, item):
        for i in range(self.cur_scope, -1, -1):
            item_list = self.dic_list[i]
            if item in item_list:
                return item_list[item]
        return None
    
    def insert_item(self, key, val):
        if key in self.dic_list[self.cur_scope]:
            return {"result": "fail", "error": "Type Redefination" }
        self.dic_list[self.cur_scope][key] = val
        return {'result': 'success'}

    def has_item(self, item):
        for i in range(self.cur_scope, -1, -1):
            item_list = self.dic_list[i]
            if item in item_list:
                return True
        return False

    def func_enter(self):
        self.cur_scope += 1
        self.dic_list.append({})

    def func_quit(self):
        if self.cur_scope == 0:
            return
        self.dic_list.pop(-1)
        self.cur_scope -= 1

    def is_global(self):
        if len(self.dic_list) == 1:
            return True
        else:
            return False
