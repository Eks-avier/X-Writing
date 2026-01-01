# STL - Unordered Maps

## The Basics

- An unordered map is an STL container.
- An unordered map stores its elements as key-value pairs.
- An unordered map uses a hash table rather than a red-black binary tree n the case of `std::map`.
- Operations on an unordered map is of average time complexity, assuming no collisions and rehashing occur.

```cpp
enum Color {
	red,
	yellow,
	purple,
	orange,
	green
};

int main() {
	std::unordered_map<std::string, Color> fruits{};
	["Apple"] = red;
	["Mango"] = yellow;
	["Grapes"] = purple;
	["Orange"] = orange;
	["Green Apple"] = green;
}
```

## Buckets and Hashing

- Internally an element of an unordered map is stored in a bucket.
- An unordered map provides a bucket interface.
- The number of buckets can be pre-allocated if the number of elements to insert is known ahead of time by using `std::unordered_map::reserve()`.
- Typically a bucket only contains one element. However, if two elements have the same hash value, then a hash collision has occurred.
- The likelihood of a hash collision occurring can be determined by the load factor.
	- The load factor is a ratio of elements to number of buckets.
	- A low load factor is ideal as there are fewer elements occupying the buckets.
	- A high load factor is dangerous as there are more elements than there buckets. This can lead to hash collisions, which in turn might lead to a rehashing, and thus degraded performance.
	- Rehashing redistributes the elements into new buckets.
- Hash collisions are resolved through either chaining or open addressing.
	- When elements are chained, they are stored in linked lists or dynamic arrays.
	- In open addressing, elements are sent to unoccupied buckets.