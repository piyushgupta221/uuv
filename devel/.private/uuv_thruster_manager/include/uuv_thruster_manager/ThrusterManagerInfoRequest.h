// Generated by gencpp from file uuv_thruster_manager/ThrusterManagerInfoRequest.msg
// DO NOT EDIT!


#ifndef UUV_THRUSTER_MANAGER_MESSAGE_THRUSTERMANAGERINFOREQUEST_H
#define UUV_THRUSTER_MANAGER_MESSAGE_THRUSTERMANAGERINFOREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace uuv_thruster_manager
{
template <class ContainerAllocator>
struct ThrusterManagerInfoRequest_
{
  typedef ThrusterManagerInfoRequest_<ContainerAllocator> Type;

  ThrusterManagerInfoRequest_()
    {
    }
  ThrusterManagerInfoRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ThrusterManagerInfoRequest_

typedef ::uuv_thruster_manager::ThrusterManagerInfoRequest_<std::allocator<void> > ThrusterManagerInfoRequest;

typedef boost::shared_ptr< ::uuv_thruster_manager::ThrusterManagerInfoRequest > ThrusterManagerInfoRequestPtr;
typedef boost::shared_ptr< ::uuv_thruster_manager::ThrusterManagerInfoRequest const> ThrusterManagerInfoRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace uuv_thruster_manager

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uuv_thruster_manager/ThrusterManagerInfoRequest";
  }

  static const char* value(const ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Copyright (c) 2016 The UUV Simulator Authors.\n"
"# All rights reserved.\n"
"#\n"
"# Licensed under the Apache License, Version 2.0 (the \"License\");\n"
"# you may not use this file except in compliance with the License.\n"
"# You may obtain a copy of the License at\n"
"#\n"
"#     http://www.apache.org/licenses/LICENSE-2.0\n"
"#\n"
"# Unless required by applicable law or agreed to in writing, software\n"
"# distributed under the License is distributed on an \"AS IS\" BASIS,\n"
"# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
"# See the License for the specific language governing permissions and\n"
"# limitations under the License.\n"
"\n"
;
  }

  static const char* value(const ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ThrusterManagerInfoRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::uuv_thruster_manager::ThrusterManagerInfoRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // UUV_THRUSTER_MANAGER_MESSAGE_THRUSTERMANAGERINFOREQUEST_H