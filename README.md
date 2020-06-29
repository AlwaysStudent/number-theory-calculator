# 信息安全中的数论专用计算平台

## 需要实现的功能

1. 欧几里得算法和逆元

   $$ \begin{aligned} {8656} &=& {1} * {7780} + {876} \\{7780} &=& {8} * {876} + {772} \\{876} &=& {1} * {772} + {104} \\{772} &=& {7} * {104} + {44} \\{104} &=& {2} * {44} + {16} \\{44} &=& {2} * {16} + {12} \\{16} &=& {1} * {12} + {4} \\{12} &=& {3} * {4} + {0} \\ \end{aligned} $$ $$ \begin{aligned} {4} &=& ({1}) * {16} + ({-1}) * {12} \\ &=& ({1}) * {16} + ({-1}) * ({44} - ({2}) * {16}) \\ &=& ({-1}) * {44} + ({3}) * {16} \\ &=& ({-1}) * {44} + ({3}) * ({104} - ({2}) * {44}) \\ &=& ({3}) * {104} + ({-7}) * {44} \\ &=& ({3}) * {104} + ({-7}) * ({772} - ({7}) * {104}) \\ &=& ({-7}) * {772} + ({52}) * {104} \\ &=& ({-7}) * {772} + ({52}) * ({876} - ({1}) * {772}) \\ &=& ({52}) * {876} + ({-59}) * {772} \\ &=& ({52}) * {876} + ({-59}) * ({7780} - ({8}) * {876}) \\ &=& ({-59}) * {7780} + ({524}) *{876} \\ &=& ({-59}) * {7780} + ({524}) * ({8656} - ({1}) * {7780}) \\ &=& ({524}) * {8656} + ({-583}) * {7780} \\ \end{aligned} $$

2. 模大数幂乘

   $$
   \begin{aligned}
   {3}^{1024} \;{mod}\; {10} \;&\equiv& \; {9}^{512} \;{mod}\; {10} \\
   &\equiv& \; {1}^{256} \;{mod}\; {10}\\
   &\equiv& \; {1}^{256} \;{mod}\; {10}\\
   \end{aligned}
   $$
   $$ \begin{aligned} {23}^{105} \;{mod}\; {31}&\equiv& \;{1}*{23} * {23}^{104} \;{mod}\; {31}\\&\equiv& \;{23}*{23}^{104} \;{mod}\; {31}\\&\equiv& \;{23}*({23} ^ {2})^{52} \;{mod}\; {31}\\&\equiv& \;{23}*{2}^{52} \;{mod}\; {31}\\&\equiv& \;{23}*({2} ^ {2})^{26} \;{mod}\; {31}\\&\equiv& \;{23}*{4}^{26} \;{mod}\; {31}\\&\equiv& \;{23}*({4} ^ {2})^{13} \;{mod}\; {31}\\&\equiv& \;{23}*{16}^{13} \;{mod}\; {31}\\&\equiv& \;{23}*{16} * {16}^{12} \;{mod}\; {31}\\&\equiv& \;{27}*{16}^{12} \;{mod}\; {31}\\&\equiv& \;{27}*({16} ^ {2})^{6} \;{mod}\; {31}\\&\equiv& \;{27}*{8}^{6} \;{mod}\; {31}\\&\equiv& \;{27}*({8} ^ {2})^{3} \;{mod}\; {31}\\&\equiv& \;{27}*{2}^{3} \;{mod}\; {31}\\&\equiv& \;{27}*{2} * {2}^{2} \;{mod}\; {31}\\&\equiv& \;{23}*{2}^{2} \;{mod}\; {31}\\&\equiv& \;{23}*({2} ^ {2})^{1} \;{mod}\; {31}\\&\equiv& \;{23}*{4}^{1} \;{mod}\; {31}\\&\equiv& \; {4} \;{mod}\; {31}\\\end{aligned} $$

3. Jacobi和Legendre符号
4. 孙子定理
5. 线性同余方程
6. 欧拉/费马定理
7. RSA计算和生成
8. 椭圆曲线
9.  E-Gimo
10. 希尔密码(矩阵)

## 需要用到的内容

1. python语言
2. Latex语言
3. 自定义每个模块的基类，设置适当的抽象方法，子类继承后分为求结果和求过程的类，在演示的时候调用求过程的类，在其他模块中调用求结果的类
4. 每个需求自定义一个模块文件
5. 一个gui库对所有模块进行整合，暂定为pyqt5
6. 部分使用多线程对运行速度进行优化
