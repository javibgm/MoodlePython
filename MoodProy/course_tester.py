'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import show
from config import info,users


def test_get_site_info():
    show(t.get_site_info())

def test_course_contents(test):
    if test == '0':
    # Manually show 1 course content 
        print 'Course ID to show contents:'
        show(t.course_contents(raw_input()))
    elif test == '1':
        show(t.course_contents('2',[{'name':'optionname','value':'valuename'}]))
    elif test == '2':
        show(t.course_contents(2))
    # Errors
    elif test == '3':
        show(t.course_contents('a'))
    elif test == '4':
        show(t.course_contents(255))
    elif test == '5':
        show(t.course_contents(2546453415))

def test_get_courses(test):
    if test == '0':
    # Manually show 1 course
        print 'Course ID to show:'
        show(t.get_courses([raw_input()]))
    elif test == '1':
        show(t.get_courses())
    elif test == '2':
        show(t.get_courses([2, 4]))
    # Errors
    elif test == '3':
        show(t.get_courses(2))
    elif test == '4':
        show(t.get_courses('24'))
    elif test == '5':
        show(t.get_courses([2, 'a']))

def test_create_courses(test):
    array=[]
    if test=='1':
        array = [{'fullname':'Python course','shortname':'PythCourse','categoryid':'1'}]
    elif test =='2':
        array = [{'fullname':'Python course1','shortname':'PythCourse1','categoryid':'1'},{'fullname':'Python course2','shortname':'PythCourse2','categoryid':'1'}]
    elif test =='3':
        array = [{'fullname':'Python course','shortname':'PythCourse','categoryid':'1', 'courseformatoptions':[{'name':'numsections','value':'10'},{'name':'hiddensections','value':'0'},{'name':'coursedisplay','value':'0'}]}]
    # Errors: try to create 2 categories with the same idnumber -> execute 2 times test 1
    elif test =='4':
        array = [{'shortname':'PythCourse','categoryid':'1'}]
    elif test =='5':
    # Add a course in a non-existent category
        array = [{'fullname':'Python course','shortname':'PythCourse','categoryid':'100001'}]
    show(t.create_courses(array))

def test_delete_courses(test):
    array=[]
    if test=='0':
    # Delete manually 1 course
        print 'Course ID to delete:'
        array=[raw_input()]
    # Errors
    elif test=='1':
        array = [-1]
    elif test=='2':
        array = ['a']
    show(t.delete_courses(array))

def test_update_courses(test):
    array=[]
    if test=='1':
        array =[{'id':'2','fullname':'Course 1 modified'}]
    # Warnings
    elif test=='2':
        array =[{'id':'200','fullname':'Course 1 modified'}]
    # Errors
    elif test=='3':
        array =[{'fullname':'Course lost'}]
    elif test=='4':
        array =[{'id':'2','categoryid':'a'}]
    show(t.update_courses(array))
    
def test_duplicate_course(test):
    if test=='1':
        show(t.duplicate_course(2, 'Course 1 copy', 'Course1copy', '1'))
    elif test=='2':
        show(t.duplicate_course(2, 'Course 1 copy', 'Course1copy', '1', 1, [{'name':'activities','value':'0'},{'name':'blocks','value':'0'},{'name':'filters','value':'0'},
                                                                            {'name':'users','value':'0'},{'name':'role_assignments','value':'0'}]))
    elif test=='3':
        show(t.duplicate_course(2, 'Course 1 copy', 'Course1copy', '1','a'))

def test_import_course(test):
    if test=='1':
    # Import all 
        show(t.import_course(2, 15))
    elif test=='2':
    # Import only activities 
        show(t.import_course(2, 15, 0,[{'name':'activities','value':'1'},{'name':'blocks','value':'0'},{'name':'filters','value':'0'}]))
    elif test=='3':
    # Delete contents and do not import anything 
        show(t.import_course(2, 15, 1,[{'name':'activities','value':'0'},{'name':'blocks','value':'0'},{'name':'filters','value':'0'}]))
    
def test_get_categories(test):
    array = []
    if test == '1':
        array = [{'key': 'id', 'value':'1'}]
    elif test == '2':
        array = [{'key': 'name', 'value':'Miscellaneous'}]
    elif test == '3':
        array = [{'key': 'parent', 'value':'0'}]
    elif test == '4':
        array = [{'key': 'idnumber', 'value':'10'}]
    elif test == '5':
        array = [{'key': 'visible', 'value':'1'}]
    elif test == '6':
        array = [{'key': 'theme', 'value':'None'}]
    elif test == '7':
        array = [{'key': 'id', 'value':'100'}]
    elif test == '8':
        array = [{'key': 'id', 'value':'a'}]
    # Errors
    elif test == '9':
        array = [{'key': 'false_key', 'value':'1'}]
    elif test == '10':
        array = [{'keys': 'id', 'values':'1'}]
    if test=='3':
    # In this case, we dont get subcategories info
        show(t.get_categories(array,0))
    else:
        show(t.get_categories(array))

def test_create_categories(test):
    array = []
    if test == '1':
        array = [{'name': 'Python Category', 'idnumber':'1', 'description':'Category created with MoodPyth'}]
    elif test == '2':
        array=[{'name': 'Python Category', 'idnumber':'2', 'description':'Category created with MoodPyth','parent':'1','descriptionformat':'0'}]
    # Errors
    elif test == '3':
        array = [{'idnumber':'1'}]
    # Error: try to create 2 categories with the same idnumber -> execute 2 times test 1
    show(t.create_categories(array))

def test_update_categories(test):
    array = []
    if test == '1':
        print 'Category ID to change name:'
        catID = raw_input()
        catName = t.get_categories([{'key': 'id', 'value':catID}])[0]['name']
        array = [{'id':catID,'name': 'CATEGORY NAME CHANGED'}]
        show(t.update_categories(array))
        print 'Category name changed. Press any key to its name be returned...'
        raw_input()
        array = [{'id':catID,'name': catName}]
    # Errors
    elif test == '2':
        array = [{'id':-1,'name': 'Error'}]
    elif test == '3':
        array = [1]
    show(t.update_categories(array))
        
def test_delete_categories(test):
    array = []
    if test=='0':
    # Delete manually 1 category
        print 'category ID to delete:'
        array=[{'id':raw_input(),'recursive':1}]
    elif test=='1':
    # create a category, inside a course and delete everything
        categoryID = t.create_categories([{'name': 'Python Category'}])[0]['id']
        t.create_courses([{'fullname':'Python course','shortname':'PythCourse','categoryid':categoryID}])
        print 'Category and course created. Press enter to continue...'
        raw_input()
        array = [{'id':categoryID,'recursive':1}]
    elif test=='2':
    # create two categories, inside one create a course, delete that category and copy the content to the second course
        categoryID1 = t.create_categories([{'name': 'Python Category'}])[0]['id']
        categoryID2 = t.create_categories([{'name': 'Python Category 2'}])[0]['id']
        t.create_courses([{'fullname':'Python course','shortname':'PythCourse','categoryid':categoryID1}])
        print 'Categories and course created. Press enter to continue... (delete category and copy the content to the other one)'
        raw_input()
        array = [{'id':categoryID1,'newparent':categoryID2}]
        show(t.delete_categories(array))
        print 'Category deleted, course moved to second category. Press enter to continue... (delete the other category and the course)'
        raw_input()
        array = [{'id':categoryID2,'recursive':1}]
    elif test=='3':
    # create two categories, one inside other one, and inside create a course. Delete the child category and copy the content to the parent
        categoryIDparent = t.create_categories([{'name': 'Python Category'}])[0]['id']
        categoryIDchild = t.create_categories([{'name': 'Python Category 2','parent':categoryIDparent}])[0]['id']
        t.create_courses([{'fullname':'Python course','shortname':'PythCourse','categoryid':categoryIDchild}])
        print 'Categories and course created. Press enter to continue... (delete category and copy the content to the parent)'
        raw_input()
        array = [{'id':categoryIDchild}]
        show(t.delete_categories(array))
        print 'Category deleted, course moved to parent category. Press enter to continue... (delete the other category and the course)'
        raw_input()
        array = [{'id':categoryIDparent,'recursive':1}]
    #Errors
    elif test=='4':
        pass
    elif test=='5':
        array = [{'id':'a'}]
    elif test=='6':
        categoryID = t.create_categories([{'name': 'Python Category'}])[0]['id'] # Category created, delete manually
        array = [{'id':categoryID}]
    elif test=='7':
        array = [3]
    elif test=='8':
        array = ['3']
    show(t.delete_categories(array))

def test_delete_modules(test):
    array = []
    if test=='0':
        # Delete 1 module manually
        print 'Module ID to delete: '
        array = [raw_input()]
    # Errors
    elif test == '1':
        array = [-1]
    elif test == '2':
        array = ['a']
    show(t.delete_modules(array))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['admin']['token'])
    #test_get_site_info()
    #test_course_contents(raw_input())
    #test_get_courses(raw_input())
    #test_create_courses(raw_input())
    #test_delete_courses(raw_input())
    #test_update_courses(raw_input())
    #test_duplicate_course(raw_input())
    #test_import_course(raw_input())
    #test_get_categories(raw_input())
    #test_create_categories(raw_input())
    #test_update_categories(raw_input())
    #test_delete_categories(raw_input())
    #test_delete_modules(raw_input())