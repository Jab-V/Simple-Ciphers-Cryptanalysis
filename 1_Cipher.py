import numpy as np

Letter=['a','b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numb_letter=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
def Convert_to_letter(mat):
   mat=Round_fun(mat)  
   MM=np.chararray((mat.shape[0], mat.shape[1]), unicode=True)
   for i in range(mat.shape[0]):
      for j in range(mat.shape[1]):   
           MM[i][j]=Letter[int(mat[i][j])]  
   return MM



def num_char(X):
  X=X.upper()
  return ord(X)-65

def text_to_num(Y):
   Y=Y.replace(' ','')
   return [num_char(i)   for i in Y]


def Mat_text(text,n_key):
   if len(text) % n_key != 0:
     for i in range(0, len(text)):
        text.append(text[i])
        if len(text) % n_key == 0:
           break
   K=0
   Out_text=np.zeros((    (len(text)// n_key)  ,n_key ))
   for i in range(len(text)// n_key):
      for j in range(n_key):
         Out_text[i][j]  =text[K]
         K=K+1
   return  Out_text


def Round_fun(mat):
   for i in range(mat.shape[0]):
      for j in range(mat.shape[1]):
           mat[i][j]=round(mat[i][j],1)
   return mat        

def Multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse

def invesre_mat(key):
  if np.linalg.det(key) == 0: print('Key is not invertible')
  else:  
         det=round(np.linalg.det(key)%26)
         det=Multiplicative_inverse(det)
         if det == -1:
            print("Determinant is not relatively prime to 26, uninvertible matrix")
         Adj=(np.linalg.inv(key)  *np.linalg.det(key) ) %26
         return Round_fun(Adj*det)%26


def Text_encryption(text,key):
   n_key=key.shape[0]  
   Matrix_text=Mat_text(text_to_num(text),n_key)
   Matrix_tex=np.matmul(Matrix_text,key)
   return Matrix_tex%26,Convert_to_letter(Matrix_tex%26)


def Text_Decryption(cipher_text,key):
   n_key=key.shape[0]  
   key_inverse=invesre_mat(key)
   Matrix_tex=np.matmul(cipher_text,key_inverse)
   return Matrix_tex%26,Convert_to_letter(Matrix_tex%26)
