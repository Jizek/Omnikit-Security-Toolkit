"""
Verification script to check Tool_Interface against design requirements.

This script verifies that the Tool_Interface implementation meets all
requirements specified in the design document.

Author: jizek
"""

from omnikit.core.tool_interface import Tool_Interface, ToolMetadata, ToolCategory
import inspect


def verify_requirements():
    """Verify Tool_Interface meets all design requirements."""
    print("=" * 70)
    print("Verifying Tool_Interface Against Design Requirements")
    print("=" * 70)
    
    requirements = []
    
    # Requirement 4.1: Base Tool_Interface exists
    print("\n[Req 4.1] Tool_Interface base class exists")
    try:
        assert inspect.isclass(Tool_Interface)
        assert inspect.isabstract(Tool_Interface)
        print("✓ Tool_Interface is an abstract base class")
        requirements.append(("4.1", True))
    except AssertionError:
        print("✗ Tool_Interface is not properly defined")
        requirements.append(("4.1", False))
    
    # Requirement 4.2: Abstract methods defined
    print("\n[Req 4.2] Abstract methods: get_metadata(), initialize(), execute(), cleanup()")
    abstract_methods = Tool_Interface.__abstractmethods__
    required_methods = {'get_metadata', 'initialize', 'execute', 'cleanup'}
    
    if required_methods.issubset(abstract_methods):
        print(f"✓ All required abstract methods present: {required_methods}")
        requirements.append(("4.2", True))
    else:
        missing = required_methods - abstract_methods
        print(f"✗ Missing abstract methods: {missing}")
        requirements.append(("4.2", False))
    
    # Requirement 4.3: ToolCategory enum exists
    print("\n[Req 4.3] ToolCategory enum with all 10 categories")
    try:
        assert inspect.isclass(ToolCategory)
        categories = [c.value for c in ToolCategory]
        expected_categories = [
            'network', 'web', 'cryptography', 'forensics', 
            'social_engineering', 'wireless', 'exploitation',
            'information_gathering', 'password_attacks', 'utilities'
        ]
        
        if set(categories) == set(expected_categories):
            print(f"✓ All 10 categories present: {len(categories)}")
            for cat in ToolCategory:
                print(f"  - {cat.name}: {cat.value}")
            requirements.append(("4.3", True))
        else:
            missing = set(expected_categories) - set(categories)
            extra = set(categories) - set(expected_categories)
            if missing:
                print(f"✗ Missing categories: {missing}")
            if extra:
                print(f"✗ Extra categories: {extra}")
            requirements.append(("4.3", False))
    except Exception as e:
        print(f"✗ ToolCategory enum error: {e}")
        requirements.append(("4.3", False))
    
    # Requirement 4.4: ToolMetadata dataclass exists
    print("\n[Req 4.4] ToolMetadata dataclass with required fields")
    try:
        from dataclasses import is_dataclass
        assert is_dataclass(ToolMetadata)
        
        # Check required fields
        fields = ToolMetadata.__dataclass_fields__
        required_fields = {
            'name', 'description', 'version', 'author',
            'categories', 'dependencies', 'keywords', 'usage_examples'
        }
        
        if required_fields.issubset(fields.keys()):
            print(f"✓ All required fields present in ToolMetadata")
            for field_name in required_fields:
                field = fields[field_name]
                print(f"  - {field_name}: {field.type}")
            requirements.append(("4.4", True))
        else:
            missing = required_fields - fields.keys()
            print(f"✗ Missing fields: {missing}")
            requirements.append(("4.4", False))
    except Exception as e:
        print(f"✗ ToolMetadata error: {e}")
        requirements.append(("4.4", False))
    
    # Requirement 4.5: Default author is "jizek"
    print("\n[Req 4.5] Default author is 'jizek'")
    try:
        fields = ToolMetadata.__dataclass_fields__
        author_field = fields['author']
        if author_field.default == "jizek":
            print("✓ Default author is 'jizek'")
            requirements.append(("4.5", True))
        else:
            print(f"✗ Default author is '{author_field.default}', expected 'jizek'")
            requirements.append(("4.5", False))
    except Exception as e:
        print(f"✗ Author field error: {e}")
        requirements.append(("4.5", False))
    
    # Additional: Helper methods
    print("\n[Additional] Helper methods: validate_dependencies(), get_help()")
    helper_methods = ['validate_dependencies', 'get_help', 'validate_input']
    tool_methods = [m for m in dir(Tool_Interface) if not m.startswith('_')]
    
    all_present = all(method in tool_methods for method in helper_methods)
    if all_present:
        print(f"✓ All helper methods present: {helper_methods}")
        requirements.append(("Helper Methods", True))
    else:
        missing = [m for m in helper_methods if m not in tool_methods]
        print(f"✗ Missing helper methods: {missing}")
        requirements.append(("Helper Methods", False))
    
    # Error handling and logging
    print("\n[Additional] Error handling and logging")
    try:
        # Check if __init__ sets up logger
        init_source = inspect.getsource(Tool_Interface.__init__)
        has_logger = 'logging.getLogger' in init_source
        has_config = '_config' in init_source
        has_metadata = '_metadata' in init_source
        
        if has_logger and has_config and has_metadata:
            print("✓ Proper initialization with logger, config, and metadata")
            requirements.append(("Error Handling", True))
        else:
            print("✗ Missing initialization components")
            requirements.append(("Error Handling", False))
    except Exception as e:
        print(f"✗ Initialization check error: {e}")
        requirements.append(("Error Handling", False))
    
    # Summary
    print("\n" + "=" * 70)
    print("Verification Summary")
    print("=" * 70)
    
    passed = sum(1 for _, result in requirements if result)
    total = len(requirements)
    
    print(f"\nTotal Requirements: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    print("\nDetailed Results:")
    for req, result in requirements:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status} - Requirement {req}")
    
    if passed == total:
        print("\n" + "=" * 70)
        print("✓ ALL REQUIREMENTS MET - Tool_Interface is complete!")
        print("=" * 70)
        return True
    else:
        print("\n" + "=" * 70)
        print("✗ Some requirements not met - review needed")
        print("=" * 70)
        return False


if __name__ == "__main__":
    success = verify_requirements()
    exit(0 if success else 1)
