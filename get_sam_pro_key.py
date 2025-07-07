#!/usr/bin/env python3
"""
SAM Pro Key Registration - Quick Start
=====================================

Simple command-line interface for new users to register and receive SAM Pro activation keys.
This script provides an easy way to get started with SAM Pro without needing to run the full web interface.

Usage:
    python get_sam_pro_key.py

Author: SAM Development Team
Version: 1.0.0
"""

import sys
import os
import json
import re
from pathlib import Path

# Add SAM to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def validate_email(email):
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    """Main registration interface."""
    print("🚀 SAM Pro Registration - Quick Start")
    print("=" * 50)
    print()
    
    # Check if key distribution system is available
    try:
        from scripts.key_distribution_system import KeyDistributionManager
        print("✅ Key distribution system available")
    except ImportError:
        print("❌ Key distribution system not available")
        print("💡 Please ensure all SAM components are properly installed")
        print()
        print("🔧 Alternative options:")
        print("1. Run the web interface: streamlit run sam_pro_registration.py")
        print("2. Generate a key manually: python scripts/generate_pro_activation_key.py")
        return 1
    
    print()
    print("🎯 Get your free SAM Pro activation key!")
    print("📧 We'll send your key via email and display it here as backup")
    print()
    
    # Collect user information
    try:
        name = input("👤 Enter your full name: ").strip()
        if not name:
            print("❌ Name is required")
            return 1
        
        email = input("📧 Enter your email address: ").strip().lower()
        if not email:
            print("❌ Email is required")
            return 1
        
        if not validate_email(email):
            print("❌ Please enter a valid email address")
            return 1
        
        organization = input("🏢 Organization (optional): ").strip()
        use_case = input("🎯 Primary use case (optional): ").strip()
        
        print()
        print("🔄 Processing your registration...")
        
        # Initialize key distribution manager
        manager = KeyDistributionManager()
        
        # Register user
        success, message, registration_id = manager.register_user(
            email=email,
            name=name,
            organization=organization or "Personal",
            use_case=use_case or "General AI assistance"
        )
        
        if not success:
            print(f"❌ Registration failed: {message}")
            return 1
        
        print(f"✅ Registration successful! ID: {registration_id}")
        
        # Assign and send key
        key_success, key_message, activation_key = manager.assign_and_send_key(registration_id)
        
        if key_success and activation_key:
            print("🎉 SAM Pro activation key generated and sent!")
            print()
            print("🔑 Your SAM Pro Activation Key:")
            print("=" * 50)
            print(f"   {activation_key}")
            print("=" * 50)
            print()
            print("📧 Key also sent to:", email)
            print()
            print("🚀 Next Steps:")
            print("1. Start SAM: python secure_streamlit_app.py")
            print("2. Navigate to: localhost:8502")
            print("3. Enter your activation key when prompted")
            print("4. Enjoy SAM Pro features!")
            print()
            print("🌟 SAM Pro Features You've Unlocked:")
            print("• TPV Active Reasoning Control - 48.4% efficiency gains")
            print("• Enhanced SLP Pattern Learning - Advanced pattern recognition")
            print("• MEMOIR Lifelong Learning - Continuous knowledge updates")
            print("• Dream Canvas - Interactive memory visualization")
            print("• Cognitive Distillation Engine - AI introspection & self-improvement")
            print("• Cognitive Automation Engine - Automated reasoning")
            print("• Advanced Memory Analytics - Deep insights")
            print("• Enhanced Web Retrieval - Premium search capabilities")
            
        else:
            print(f"⚠️ Key generation failed: {key_message}")
            print("💡 You can try again later or use the web interface:")
            print("   streamlit run sam_pro_registration.py")
            return 1
        
        print()
        print("🎯 Registration Complete!")
        print("💡 Save your activation key - you'll need it to activate SAM Pro")
        print()
        print("❓ Questions? Contact: vin@forge1825.net")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n👋 Registration cancelled by user")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("💡 Please try the web interface: streamlit run sam_pro_registration.py")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
