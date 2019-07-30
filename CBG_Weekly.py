import CBG_SalesWeekly
import CBG_GLDetail
import FF_Employees
import FF_OpCode


def weeklyrun():
    CBG_SalesWeekly.salesweekly()
    CBG_GLDetail.gldetail()


weeklyrun()

