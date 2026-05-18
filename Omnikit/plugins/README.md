# Omnikit Plugins Directory

This directory is for user-created plugins that extend Omnikit functionality.

## Creating a Plugin

1. Create a Python file in this directory
2. Implement the `Tool_Interface` from `omnikit.core.tool_interface`
3. Omnikit will automatically discover and register your plugin

## Example Plugin Structure

```python
from omnikit.core.tool_interface import Tool_Interface, ToolMetadata, ToolCategory

class MyCustomTool(Tool_Interface):
    def get_metadata(self):
        return ToolMetadata(
            name="my_custom_tool",
            description="My custom security tool",
            version="1.0.0",
            author="jizek",
            categories=[ToolCategory.UTILITIES]
        )
    
    def initialize(self, config):
        return True
    
    def execute(self, **kwargs):
        # Your tool logic here
        pass
    
    def cleanup(self):
        pass
```

Author: jizek
