from django import forms
from.models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields=('fullname','mobile','emp_code','position')
        labels={
            'fullname':'Full Name',
            'emp_code':'EMP. code'
        }
    
    def __init__(self,*args,**kwargs):#this is init function of python
        super(EmployeeForm,self).__init__(*args,**kwargs)# this is constructor of Employee form 
        self.fields['position'].empty_label="Select" # To remove the empty level ----- with select for drop down
        self.fields['emp_code'].required=False # This is for emp code block to make it require false