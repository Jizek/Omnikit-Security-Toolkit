"""
Tool_Interface - Base interface for all Omnikit tools.

This module provides the abstract base class that all Omnikit tools must implement,
ensuring consistent behavior and interface across the toolkit.

Author: jizek
Version: 2.0.0
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import logging


class ToolCategory(Enum):
    """Enumeration of tool categories in Omnikit."""
    NETWORK = "network"
    WEB = "web"
    CRYPTOGRAPHY = "cryptography"
    FORENSICS = "forensics"
    SOCIAL_ENGINEERING = "social_engineering"
    WIRELESS = "wireless"
    EXPLOITATION = "exploitation"
    INFORMATION_GATHERING = "information_gathering"
    PASSWORD_ATTACKS = "password_attacks"
    UTILITIES = "utilities"


@dataclass
class ToolMetadata:
    """
    Metadata for an Omnikit tool.
    
    Attributes:
        name: Unique identifier for the tool (lowercase with underscores)
        description: Brief description of what the tool does
        version: Tool version string (e.g., "1.0.0")
        author: Tool author (defaults to "jizek")
        categories: List of categories this tool belongs to
        dependencies: List of Python package dependencies
        keywords: List of keywords for search functionality
        usage_examples: List of usage example strings
    """
    name: str
    description: str
    version: str
    author: str = "jizek"
    categories: List[ToolCategory] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)
    usage_examples: List[str] = field(default_factory=list)


class Tool_Interface(ABC):
    """
    Abstract base class that all Omnikit tools must implement.
    
    This interface ensures consistent behavior across all tools in the Omnikit
    ecosystem. Tools must implement the abstract methods: get_metadata(),
    initialize(), execute(), and cleanup().
    
    Example:
        class MyTool(Tool_Interface):
            def get_metadata(self) -> ToolMetadata:
                return ToolMetadata(
                    name="my_tool",
                    description="Does something useful",
                    version="1.0.0",
                    categories=[ToolCategory.UTILITIES]
                )
            
            def initialize(self, config: Dict[str, Any]) -> bool:
                self._config = config
                return True
            
            def execute(self, **kwargs) -> Any:
                # Tool implementation
                return result
            
            def cleanup(self) -> None:
                # Cleanup resources
                pass
    """
    
    def __init__(self):
        """Initialize the tool interface."""
        self._metadata: Optional[ToolMetadata] = None
        self._config: Dict[str, Any] = {}
        self._logger = logging.getLogger(f"omnikit.tool.{self.__class__.__name__}")
    
    @abstractmethod
    def get_metadata(self) -> ToolMetadata:
        """
        Return tool metadata including name, description, and categories.
        
        This method must be implemented by all tools to provide information
        about the tool for discovery and documentation purposes.
        
        Returns:
            ToolMetadata: Complete metadata for this tool
        
        Example:
            def get_metadata(self) -> ToolMetadata:
                return ToolMetadata(
                    name="port_scanner",
                    description="Scans IP addresses for open ports",
                    version="2.0.0",
                    categories=[ToolCategory.NETWORK, ToolCategory.INFORMATION_GATHERING],
                    dependencies=["socket"],
                    keywords=["port", "scan", "network", "tcp"]
                )
        """
        pass
    
    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> bool:
        """
        Initialize the tool with configuration settings.
        
        This method is called before execute() to set up the tool with
        user configuration and prepare any necessary resources.
        
        Args:
            config: Dictionary of configuration key-value pairs
        
        Returns:
            bool: True if initialization was successful, False otherwise
        
        Example:
            def initialize(self, config: Dict[str, Any]) -> bool:
                self._config = config
                self._timeout = config.get('timeout', 2.0)
                self._threads = config.get('threads', 100)
                return True
        """
        pass
    
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool's main functionality.
        
        This is the core method that performs the tool's primary task.
        Parameters are passed as keyword arguments and should be validated
        before use.
        
        Args:
            **kwargs: Tool-specific parameters
        
        Returns:
            Any: Tool execution results (format varies by tool)
        
        Raises:
            ValueError: If required parameters are missing or invalid
            RuntimeError: If execution fails
        
        Example:
            def execute(self, target_ip: str, port_range: str, **kwargs) -> Dict:
                if not target_ip:
                    raise ValueError("target_ip is required")
                
                # Perform scanning
                results = self._scan_ports(target_ip, port_range)
                return results
        """
        pass
    
    @abstractmethod
    def cleanup(self) -> None:
        """
        Perform cleanup operations after execution.
        
        This method is called after execute() completes (successfully or not)
        to release resources, close connections, and perform any necessary
        cleanup operations.
        
        Example:
            def cleanup(self) -> None:
                if hasattr(self, '_connection'):
                    self._connection.close()
                if hasattr(self, '_temp_files'):
                    for f in self._temp_files:
                        f.unlink()
        """
        pass
    
    def validate_dependencies(self) -> List[str]:
        """
        Check if all required dependencies are available.
        
        This method attempts to import all dependencies listed in the tool's
        metadata and returns a list of any that are missing.
        
        Returns:
            List[str]: List of missing dependency names (empty if all present)
        
        Example:
            missing = tool.validate_dependencies()
            if missing:
                print(f"Missing dependencies: {', '.join(missing)}")
                print(f"Install with: pip install {' '.join(missing)}")
        """
        missing = []
        metadata = self.get_metadata()
        
        if metadata.dependencies:
            for dep in metadata.dependencies:
                try:
                    __import__(dep)
                except ImportError:
                    missing.append(dep)
                    self._logger.warning(f"Missing dependency: {dep}")
        
        return missing
    
    def validate_input(self, **kwargs) -> bool:
        """
        Validate input parameters before execution.
        
        This is a helper method that tools can override to provide custom
        input validation logic. The default implementation always returns True.
        
        Args:
            **kwargs: Parameters to validate
        
        Returns:
            bool: True if inputs are valid, False otherwise
        
        Example:
            def validate_input(self, **kwargs) -> bool:
                if 'target_ip' not in kwargs:
                    self._logger.error("target_ip parameter is required")
                    return False
                
                ip = kwargs['target_ip']
                if not self._is_valid_ip(ip):
                    self._logger.error(f"Invalid IP address: {ip}")
                    return False
                
                return True
        """
        return True
    
    def get_help(self) -> str:
        """
        Return formatted help text for the tool.
        
        This method generates user-friendly documentation based on the tool's
        metadata, including description, categories, and usage examples.
        
        Returns:
            str: Formatted help text
        
        Example:
            help_text = tool.get_help()
            print(help_text)
        """
        metadata = self.get_metadata()
        
        help_text = f"""
{'=' * 70}
Tool: {metadata.name}
{'=' * 70}

Description:
  {metadata.description}

Version: {metadata.version}
Author: {metadata.author}

Categories:
  {', '.join([c.value for c in metadata.categories])}
"""
        
        if metadata.keywords:
            help_text += f"""
Keywords:
  {', '.join(metadata.keywords)}
"""
        
        if metadata.dependencies:
            help_text += f"""
Dependencies:
  {', '.join(metadata.dependencies)}
"""
        
        if metadata.usage_examples:
            help_text += """
Usage Examples:
"""
            for example in metadata.usage_examples:
                help_text += f"  {example}\n"
        
        help_text += f"\n{'=' * 70}\n"
        
        return help_text
    
    def __str__(self) -> str:
        """Return string representation of the tool."""
        metadata = self.get_metadata()
        return f"<{self.__class__.__name__}: {metadata.name} v{metadata.version}>"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the tool."""
        metadata = self.get_metadata()
        return (f"{self.__class__.__name__}(name='{metadata.name}', "
                f"version='{metadata.version}', author='{metadata.author}')")
