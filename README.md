# generate-properties-vim-plugin
Vim plugin to generate JavaFX properties.

At my workplace, we use the same convention as the core JavaFX libraries; a
private property, with public methods to get and set the value, and get the
property itself. 

Example String property:

```java
private StringProperty firstName = new SimpleStringProperty(this, "firstName");
public StringProperty firstNameProperty() {return this.firstName;}
public String getFirstName() {return this.firstName.get();}
public void setFirstName(String firstName) {this.firstName.set(firstName);}
```

This extension generated the above with:

```
:GenProp String firstName
```

Takes a type as a third argument:

```
:GenProp List employees Person
```

```java
private ListProperty<Person> employees = new SimpleListProperty<>(this, "employees");
public ListProperty<Person> employeesProperty() {return this.employees;}
public ObservableList<Person> getEmployees() {return this.employees.get();}
public void setEmployees(ObservableList<Person> employees) {this.employees.set(employees);}
```

Also note that with lists, it helpfully uses `ObservableList` as the getter/setter type.
