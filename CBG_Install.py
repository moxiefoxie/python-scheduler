import CBG_SalesInstall
import CBG_GLDetail
import CBG_Employees
import CBG_OpCode



def installrun():
    CBG_SalesInstall.salesinstall()
    CBG_GLDetail.gldetail()
    CBG_Employees.employees()
    CBG_OpCode.opcode()


installrun()


