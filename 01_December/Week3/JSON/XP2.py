# 🌟 Exercise 2: Working with JSON
# =========================================================

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


def json_exercise_save_modified(birth_date: str = "1999-12-31", out_file: str = "modified_employee.json") -> None:
    """
    Loads JSON, prints nested salary, adds birth_date to employee, saves to file.
    """
    # Step 1: Load JSON string
    data = json.loads(sampleJson)

    # Step 2: Access nested salary
    salary = data["company"]["employee"]["payable"]["salary"]
    print("\nJSON Exercise")
    print("Salary:", salary)

    # Step 3: Add birth_date
    data["company"]["employee"]["birth_date"] = birth_date

    # Step 4: Save modified JSON to file
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Modified JSON saved to: {Path(out_file).resolve()}")


# =========================================================
# Run
# =========================================================

if __name__ == "__main__":
    # Exercise 1
    main()

    # Exercise 2
    json_exercise_save_modified(birth_date="2001-09-07", out_file="modified_employee.json")
