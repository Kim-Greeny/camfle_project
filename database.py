import pyrebase
import json

class DBhandler:
    def __init__(self ):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f )

            firebase = pyrebase.initialize_app(config)
            self.db = firebase.database()
            
    def insert_item(self, name, data, img_path):
        item_info ={
            "seller": data['seller'],
            "addr": data['addr'],
            "email": data['email'],
            "category": data['category'],
            "card": data['card'],
            "status": data['status'],
            "phone": data['phone'],
            "img_path": img_path
        }
        self.db.child("item").child(name).set(item_info)
        print(data,img_path)
        return True
    
    def insert_user(self, data, pw):
        user_info ={
            "id": data['id'],
            "pw": pw,
            "nickname": data['nickname']
        }
        if self.user_duplicate_check(str(data['id'])):
            self.db.child("user").push(user_info)
            print(data)
            return True
        else:
            return False
        
    def user_duplicate_check(self, id_string):
        users = self.db.child("user").get()
        
        print("users###",users.val())
        if str(users.val()) == "None": # first registration
            return True
        else:
            for res in users.each():
                value = res.val()
                
                if value['id'] == id_string:
                    return False
                return True
            
    def find_user(self, id_, pw_):
        users = self.db.child("user").get()
        target_value=[]
        for res in users.each():
            value = res.val()
            
            if value['id'] == id_ and value['pw'] == pw_:
                return True
            return False
    def get_items(self):
        items=self.db.child("item").get().val()
        return items
    
    def get_items_bycategory(self,cate):
        items=self.db.child("item").get()
        target_value=[]
        target_key=[]
        for res in items.each():
            value=res.val()
            key_value=res.key()
            
            if value['category'] == cate:
                target_value.append(value)
                target_key.append(key_value)
        print("######target_value", target_value)
        new_dict={}
            
        for k,v in zip(target_key, target_value):
             new_dict[k]=v
                
        return new_dict
    
    def get_item_byname(self, name):
        items = self.db.child("item").get()
        target_value=""
        print("###########",name)
        for res in items.each():
            key_value = res.key()
            if key_value == name:
                target_value=res.val()
                return target_value
            
    def reg_review(self, data, img_path):
<<<<<<< HEAD
        review_info = {
=======
        review_info ={
            "title": data['title'],
>>>>>>> upstream/week11-2
            "rate": data['reviewStar'],
            "review": data['reviewContents'],
            "img_path": img_path
        }
        self.db.child("review").child(data['name']).set(review_info)
        return True
    
<<<<<<< HEAD
=======
    def get_reviews(self ):
        reviews = self.db.child("review").get().val()
        return reviews
    
>>>>>>> upstream/week11-2
    def get_review_byname(self, name):
        reviews = self.db.child("review").get()
        target_value=""
        print("#########", name)
        for res in reviews.each():
            key_value = res.key()
            if key_value == name:
                target_value=res.val()
                return target_value
<<<<<<< HEAD
        
    def get_reviews(self):
        reviews = self.db.child("review").get().val()
        return reviews
    
=======
>>>>>>> upstream/week11-2
    def get_heart_byname(self, uid, name):
        hearts = self.db.child("heart").child(uid).get()
        target_value=""
        if hearts.val() == None:
            return target_value
<<<<<<< HEAD
    
=======
        
>>>>>>> upstream/week11-2
        for res in hearts.each():
            key_value = res.key()
            
            if key_value == name:
                target_value=res.val()
        return target_value
<<<<<<< HEAD

    def update_heart(self, user_id, isHeart, item):
        heart_info ={
            "interested": isHeart
        }
        self.db.child("heart").child(user_id).child(item).set(heart_info)
        return True
=======
    
    def update_heart(self, user_id, isHeart, item):
                heart_info ={
                    "interested": isHeart
                }
                self.db.child("heart").child(user_id).child(item).set(heart_info)
                return True
    
    
>>>>>>> upstream/week11-2
