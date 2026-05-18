"""
Example tool demonstrating Tool_Interface implementation.

This is a simple example showing how to create a tool that implements
the Tool_Interface base class.

Author: jizek
"""

import sys
from pathlib import Path

# Add parent directory to path to import omnikit
sys.path.insert(0, str(Path(__file__).parent.parent))

from omnikit.core.tool_interface import Tool_Interface, ToolMetadata, ToolCategory
from typing import Dict, Any
import logging


class ExampleTool(Tool_Interface):
    """
    Example tool that demonstrates proper Tool_Interface implementation.
    
    This tool performs a simple echo operation, returning the input
    parameters along with a greeting message.
    """
    
    def __init__(self):
        """Initialize the example tool."""
        super().__init__()
        self._greeting = "Hello from Omnikit!"
    
    def get_metadata(self) -> ToolMetadata:
        """Return tool metadata."""
        return ToolMetadata(
            name="example_tool",
            description="A simple example tool that echoes input and provides a greeting",
            version="1.0.0",
            author="jizek",
            categories=[ToolCategory.UTILITIES],
            dependencies=[],  # No external dependencies
            keywords=["example", "demo", "echo", "test"],
            usage_examples=[
                "omnikit run example_tool --message 'Hello World'",
                "omnikit run example_tool --message 'Test' --uppercase"
            ]
        )
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        """
        Initialize the tool with configuration.
        
        Args:
            config: Configuration dictionary
        
        Returns:
            bool: True if initialization successful
        """
        self._config = config
        
        # Get custom greeting from config if provided
        if 'greeting' in config:
            self._greeting = config['greeting']
            self._logger.info(f"Using custom greeting: {self._greeting}")
        
        self._logger.info("Example tool initialized successfully")
        return True
    
    def validate_input(self, **kwargs) -> bool:
        """
        Validate input parameters.
        
        Args:
            **kwargs: Input parameters to validate
        
        Returns:
            bool: True if inputs are valid
        """
        if 'message' not in kwargs:
            self._logger.error("Required parameter 'message' is missing")
            return False
        
        message = kwargs['message']
        if not isinstance(message, str):
            self._logger.error("Parameter 'message' must be a string")
            return False
        
        if len(message) == 0:
            self._logger.error("Parameter 'message' cannot be empty")
            return False
        
        return True
    
    def execute(self, **kwargs) -> Dict[str, Any]:
        """
        Execute the tool's main functionality.
        
        Args:
            message: The message to echo
            uppercase: Optional flag to convert message to uppercase
        
        Returns:
            Dict containing the greeting and echoed message
        
        Raises:
            ValueError: If required parameters are missing or invalid
        """
        # Validate inputs
        if not self.validate_input(**kwargs):
            raise ValueError("Invalid input parameters")
        
        message = kwargs['message']
        uppercase = kwargs.get('uppercase', False)
        
        # Process the message
        if uppercase:
            message = message.upper()
            self._logger.info("Converting message to uppercase")
        
        # Create result
        result = {
            'greeting': self._greeting,
            'echo': message,
            'length': len(message),
            'uppercase_applied': uppercase
        }
        
        self._logger.info(f"Processed message: {message}")
        return result
    
    def cleanup(self) -> None:
        """Perform cleanup operations."""
        self._logger.info("Example tool cleanup completed")
        # No resources to clean up in this simple example


def main():
    """Demonstrate the example tool usage."""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(name)s: %(message)s'
    )
    
    # Create tool instance
    tool = ExampleTool()
    
    # Display help
    print(tool.get_help())
    
    # Initialize with configuration
    config = {'greeting': 'Welcome to Omnikit!'}
    if not tool.initialize(config):
        print("Failed to initialize tool")
        return
    
    # Execute with parameters
    try:
        result = tool.execute(message="Hello, World!", uppercase=False)
        print("\nExecution Result:")
        print(f"  Greeting: {result['greeting']}")
        print(f"  Echo: {result['echo']}")
        print(f"  Length: {result['length']}")
        print(f"  Uppercase Applied: {result['uppercase_applied']}")
        
        # Execute again with uppercase
        result2 = tool.execute(message="Hello, World!", uppercase=True)
        print("\nExecution Result (uppercase):")
        print(f"  Greeting: {result2['greeting']}")
        print(f"  Echo: {result2['echo']}")
        print(f"  Length: {result2['length']}")
        print(f"  Uppercase Applied: {result2['uppercase_applied']}")
        
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        # Always cleanup
        tool.cleanup()


if __name__ == '__main__':
    main()
