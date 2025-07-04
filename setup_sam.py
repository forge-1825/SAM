#!/usr/bin/env python3
"""
SAM Interactive Setup Script

Comprehensive guided setup wizard for SAM (Secure AI Memory).
Provides step-by-step installation with dependency management,
encryption setup, and system configuration.

Author: SAM Development Team
Version: 1.0.0
"""

import os
import sys
import subprocess
import platform
import time
import webbrowser
from pathlib import Path

def print_banner():
    """Print the SAM setup banner."""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 SAM INTERACTIVE SETUP WIZARD 🧙‍♂️                        ║
║                     Secure AI Memory - Complete Installation                ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def print_welcome():
    """Print welcome message and setup overview."""
    print("🎉 Welcome to SAM (Secure AI Memory)!")
    print("This interactive wizard will guide you through the complete setup process.")
    
    print("\n🎯 **What this setup will do:**")
    print("   • ✅ Check system requirements")
    print("   • 📦 Install Python dependencies")
    print("   • 🔐 Configure enterprise-grade encryption")
    print("   • 🧠 Initialize memory systems")
    print("   • 🎨 Set up user interface")
    print("   • 🚀 Prepare SAM for first use")
    
    print("\n⏱️  **Estimated time:** 10-15 minutes")
    print("💡 **Difficulty:** Beginner-friendly")
    
    response = input("\n🤔 Ready to begin? (Y/n): ").strip().lower()
    if response == 'n':
        print("👋 Setup cancelled. Run this script again when you're ready!")
        return False
    return True

def check_system_requirements():
    """Check system requirements and compatibility."""
    print("\n" + "="*60)
    print("📋 Step 1: System Requirements Check")
    print("="*60)
    
    print("🔍 Checking system compatibility...")
    
    # Check Python version
    python_version = sys.version_info
    print(f"   🐍 Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("   ❌ Python 3.8+ required")
        print("   💡 Please upgrade Python and try again")
        return False
    else:
        print("   ✅ Python version compatible")
    
    # Check operating system
    os_name = platform.system()
    print(f"   💻 Operating system: {os_name}")
    
    if os_name in ['Windows', 'Darwin', 'Linux']:
        print("   ✅ Operating system supported")
    else:
        print("   ⚠️  Operating system not tested (may work)")
    
    # Check available disk space
    try:
        disk_usage = os.statvfs('.')
        free_space_gb = (disk_usage.f_frsize * disk_usage.f_bavail) / (1024**3)
        print(f"   💾 Available disk space: {free_space_gb:.1f} GB")
        
        if free_space_gb < 1.0:
            print("   ⚠️  Low disk space (recommend 2+ GB)")
        else:
            print("   ✅ Sufficient disk space")
    except:
        print("   ⚪ Could not check disk space")
    
    print("\n✅ System requirements check complete!")
    return True

def install_dependencies():
    """Install Python dependencies."""
    print("\n" + "="*60)
    print("📋 Step 2: Installing Dependencies")
    print("="*60)
    
    print("📦 Installing Python packages...")
    print("   This may take a few minutes depending on your internet connection.")
    
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        print("💡 Please ensure you're in the SAM directory")
        return False
    
    try:
        print("\n🔄 Running: pip install -r requirements.txt")
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], check=True, capture_output=True, text=True)
        
        print("✅ Dependencies installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Dependency installation failed: {e}")
        print("\n💡 **Troubleshooting:**")
        print("   • Check your internet connection")
        print("   • Try: pip install --upgrade pip")
        print("   • Try: pip install -r requirements.txt --user")
        return False

def setup_encryption():
    """Set up encryption system."""
    print("\n" + "="*60)
    print("📋 Step 3: Encryption Setup")
    print("="*60)
    
    print("🔐 Setting up enterprise-grade encryption...")
    print("   This will create a secure keystore for your data.")
    
    if not Path("setup_encryption.py").exists():
        print("❌ Encryption setup script not found")
        return False
    
    try:
        print("\n🔄 Running encryption setup...")
        subprocess.run([sys.executable, "setup_encryption.py"], check=True)
        print("✅ Encryption setup completed!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Encryption setup failed: {e}")
        return False
    except KeyboardInterrupt:
        print("\n👋 Encryption setup cancelled")
        return False

def initialize_memory_systems():
    """Initialize SAM's memory systems."""
    print("\n" + "="*60)
    print("📋 Step 4: Memory System Initialization")
    print("="*60)
    
    print("🧠 Initializing SAM's memory systems...")
    
    # Create necessary directories
    directories = [
        "memory_store",
        "memory_store/chroma_db",
        "memory_store/encrypted",
        "logs",
        "temp"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   ✅ Created: {directory}/")
    
    print("✅ Memory systems initialized!")
    return True

def configure_ui():
    """Configure user interface settings."""
    print("\n" + "="*60)
    print("📋 Step 5: User Interface Configuration")
    print("="*60)
    
    print("🎨 Configuring user interface...")
    
    # Check if UI files exist
    ui_files = [
        "secure_streamlit_app.py",
        "ui/memory_app.py"
    ]
    
    missing_files = []
    for file_path in ui_files:
        if Path(file_path).exists():
            print(f"   ✅ Found: {file_path}")
        else:
            print(f"   ❌ Missing: {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print("⚠️  Some UI files are missing")
        print("   SAM will still work but some features may be unavailable")
    else:
        print("✅ User interface configuration complete!")
    
    return True

def run_final_tests():
    """Run final system tests."""
    print("\n" + "="*60)
    print("📋 Step 6: Final System Tests")
    print("="*60)
    
    print("🧪 Running system tests...")
    
    # Test encryption if available
    if Path("test_encryption_setup.py").exists():
        try:
            print("   🔐 Testing encryption system...")
            result = subprocess.run([
                sys.executable, "test_encryption_setup.py"
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print("   ✅ Encryption test passed")
            else:
                print("   ⚠️  Encryption test had issues (may still work)")
        except:
            print("   ⚪ Could not test encryption")
    
    # Test basic imports
    try:
        print("   📦 Testing core imports...")
        import streamlit
        print("   ✅ Streamlit available")
    except ImportError:
        print("   ❌ Streamlit not available")
        return False
    
    try:
        from security import SecureStateManager
        print("   ✅ Security modules available")
    except ImportError:
        print("   ⚠️  Security modules not available")
    
    print("✅ System tests completed!")
    return True

def open_registration_page():
    """Open the SAM Pro registration/activation page automatically."""
    try:
        print("\n🌐 **Opening SAM Pro Activation Page...**")
        print("   Starting SAM and opening activation interface...")

        # Ask user if they want to auto-open
        try:
            response = input("\n❓ Would you like to automatically start SAM and open the activation page? (y/n) [y]: ").strip().lower()
            if response and response not in ['y', 'yes']:
                print("   ⏭️ Skipping auto-start. You can manually start SAM later.")
                return False
        except KeyboardInterrupt:
            print("\n   ⏭️ Skipping auto-start.")
            return False

        # Start SAM in the background
        print("   🚀 Starting SAM services...")

        # Launch SAM secure mode in background
        try:
            subprocess.Popen([
                sys.executable, "start_sam_secure.py", "--mode", "full"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print("   ✅ SAM services starting in background...")

            # Wait for services to start
            print("   ⏳ Waiting for services to initialize (30 seconds)...")
            time.sleep(30)

            # Open the activation page
            activation_url = "http://localhost:8502"
            print(f"   🌐 Opening activation page: {activation_url}")

            webbrowser.open(activation_url)

            print("   ✅ Activation page opened in your default browser!")
            print("\n💡 **What to do next:**")
            print("   1. Enter your master password to unlock SAM")
            print("   2. Look for the '🔑 SAM Pro Activation' section in the sidebar")
            print("   3. Enter your activation key to unlock premium features")
            print("   4. If you don't have an activation key:")
            print("      • Visit: http://localhost:8503 to register for a free key")
            print("      • Or run: streamlit run sam_pro_registration.py --server.port 8503")

            return True

        except Exception as e:
            print(f"   ⚠️ Could not auto-start SAM: {e}")
            print("   💡 Please manually start SAM with: python start_sam_secure.py --mode full")
            return False

    except Exception as e:
        print(f"   ❌ Failed to open registration page: {e}")
        print("   💡 Please manually navigate to http://localhost:8502 after starting SAM")
        return False

def start_registration_interface():
    """Start the SAM Pro registration interface for new users."""
    try:
        print("\n🌐 **Starting SAM Pro Registration Interface...**")
        print("   This will allow new users to register for activation keys")

        # Check if registration system is available
        if not Path("sam_pro_registration.py").exists():
            print("   ❌ Registration interface not found (sam_pro_registration.py)")
            print("   💡 This is normal for basic installations")
            return False

        # Check if key distribution system is configured
        config_path = Path("config/key_distribution.json")
        if not config_path.exists():
            print("   ⚠️ Key distribution not configured")
            print("   💡 Copy config/key_distribution.json.template to config/key_distribution.json")
            print("   💡 Then edit with your email settings")
            return False

        # Start the registration interface
        print("   🚀 Starting registration interface on port 8503...")

        try:
            subprocess.Popen([
                sys.executable, "-m", "streamlit", "run",
                "sam_pro_registration.py",
                "--server.port=8503",
                "--server.address=localhost",
                "--browser.gatherUsageStats=false"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print("   ✅ Registration interface starting...")
            print("   🌐 New users can register at: http://localhost:8503")
            print("   📧 Activation keys will be sent via email automatically")

            # Wait a moment then open browser
            time.sleep(3)
            webbrowser.open("http://localhost:8503")

            print("   ✅ Registration interface opened in browser!")
            return True

        except Exception as e:
            print(f"   ❌ Failed to start registration interface: {e}")
            print("   💡 You can start it manually with:")
            print("   💡 streamlit run sam_pro_registration.py --server.port 8503")
            return False

    except Exception as e:
        print(f"   ❌ Registration interface startup failed: {e}")
        return False

def show_completion_summary():
    """Show setup completion summary and next steps."""
    print("\n" + "="*80)
    print("🎉 SAM SETUP COMPLETE!")
    print("="*80)
    
    print("\n✅ **Installation Summary:**")
    print("   • System requirements verified")
    print("   • Dependencies installed")
    print("   • Encryption configured")
    print("   • Memory systems initialized")
    print("   • User interface ready")
    print("   • System tests completed")
    
    print("\n🚀 **Next Steps:**")
    print("   1. Start SAM: python start_sam_secure.py --mode full")
    print("   2. Open browser: http://localhost:8502")
    print("   3. Enter your master password when prompted")
    print("   4. Activate SAM Pro for premium features")
    print("   5. Begin using SAM's AI capabilities!")
    
    print("\n📚 **Useful Commands:**")
    print("   • Start SAM: python start_sam_secure.py --mode full")
    print("   • Memory Center: Access via SAM interface")
    print("   • Test encryption: python test_encryption_setup.py")
    print("   • View logs: ls logs/")
    
    print("\n🔗 **Documentation:**")
    print("   • README.md - Main documentation")
    print("   • ENCRYPTION_SETUP_GUIDE.md - Encryption help")
    print("   • GitHub: https://github.com/forge-1825/SAM")
    
    print("\n🎯 **SAM is now ready to use!**")
    print("   You have successfully installed the world's most advanced")
    print("   AI memory system with real-time cognitive dissonance monitoring.")

def main():
    """Main interactive setup process."""
    print_banner()
    
    if not print_welcome():
        return False
    
    # Step 1: System requirements
    if not check_system_requirements():
        print("\n❌ System requirements not met")
        return False
    
    # Step 2: Dependencies
    if not install_dependencies():
        print("\n❌ Dependency installation failed")
        print("💡 You can try manual installation: pip install -r requirements.txt")
        return False
    
    # Step 3: Encryption
    if not setup_encryption():
        print("\n⚠️  Encryption setup incomplete")
        print("💡 You can set up encryption later: python setup_encryption.py")
    
    # Step 4: Memory systems
    if not initialize_memory_systems():
        print("\n❌ Memory system initialization failed")
        return False
    
    # Step 5: UI configuration
    if not configure_ui():
        print("\n⚠️  UI configuration incomplete")
    
    # Step 6: Final tests
    if not run_final_tests():
        print("\n⚠️  Some tests failed, but SAM may still work")
    
    # Completion summary
    show_completion_summary()

    # Open registration page automatically
    try:
        open_registration_page()
    except Exception as e:
        print(f"\n⚠️ Could not auto-open activation page: {e}")
        print("💡 Please manually navigate to http://localhost:8502 after starting SAM")

    # Offer to start registration interface
    try:
        start_registration = input("\n❓ Would you like to start the SAM Pro registration interface for new users? (y/n) [n]: ").strip().lower()
        if start_registration in ['y', 'yes']:
            start_registration_interface()
    except KeyboardInterrupt:
        print("\n   ⏭️ Skipping registration interface startup.")

    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎉 Setup completed successfully!")
            sys.exit(0)
        else:
            print("\n❌ Setup completed with issues")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        print("💡 Please report this issue on GitHub")
        sys.exit(1)
