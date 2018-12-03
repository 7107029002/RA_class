matrix=[0.63,0.17,0.2]
matrix1=[[0.5,0.375,0.125],[0.25,0.125,0.625],[0.25,0.375,0.375]]
matrix2=[[0.6,0.2,0.15,0.05],[0.25,0.25,0.25,0.25],[0.05,0.1,0.35,0.5]]
a1s=matrix[0]*matrix2[0][0]
a1c=matrix[1]*matrix2[1][0]
a1r=matrix[2]*matrix2[2][0]
print('a1(S)=',a1s)
print('a1(C)=',a1c)
print('a1(R)=',a1r)

a2s=(a1s*matrix1[0][0]+a1c*matrix1[1][0]+a1r*matrix1[2][0])*matrix2[0][1]
a2c=(a1s*matrix1[0][1]+a1c*matrix1[1][1]+a1r*matrix1[2][1])*matrix2[1][1]
a2r=(a1s*matrix1[0][2]+a1c*matrix1[1][2]+a1r*matrix1[2][2])*matrix2[2][1]
print('a2(S)=',a2s)
print('a2(C)=',a2c)
print('a2(R)=',a2r)

a3s=(a2s*matrix1[0][0]+a2c*matrix1[1][0]+a2r*matrix1[2][0])*matrix2[0][2]
a3c=(a2s*matrix1[0][1]+a2c*matrix1[1][1]+a2r*matrix1[2][1])*matrix2[1][2]
a3r=(a2s*matrix1[0][2]+a2c*matrix1[1][2]+a2r*matrix1[2][2])*matrix2[2][2]
print('a3(S)=',a3s)
print('a3(C)=',a3c)
print('a3(R)=',a3r)